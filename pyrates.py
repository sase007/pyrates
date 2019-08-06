#!/usr/bin/env python3

import requests, sys, json

def get_rates(base_currency = "", currencies = "", single_date = "", date_interval = [""], print_debug = False, return_dict = True):
    
    if isinstance(base_currency, str):
        base_currency = base_currency.upper()
    else:
        print("Unexpected base_currency variable type. Str expected" + str(type(base_currency)) + " given.")
        sys.exit(1)
    
    if isinstance(currencies, list) or isinstance(currencies, str):
        if isinstance(currencies, list) and len(currencies) > 1:
            currencies = [currency.upper() for currency in currencies]
            for currency in currencies:
                if base_currency in currency and base_currency != "":
                    print("Currencies cannot contain base currency!")
                    sys.exit(1)
        elif isinstance(currencies, list) and len(currencies) == 1:
            currencies = currencies[0].upper()
            if base_currency in currencies and base_currency != "":
                print("Currencies cannot contain base currency!")
                sys.exit(1)
        elif isinstance(currencies, str):
            currencies = currencies.upper()
            if base_currency in currencies and base_currency != "":
                print("Currencies cannot contain base currency!")
                sys.exit(1)
    else:
        print("Unexpected currencies variable type. Str or list expected, " + str(type(currencies)) + "given.")
        sys.exit(1)

    url = 'https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(base_currency, currencies).replace(" ", "").replace("[", "").replace("]", "").replace("'", "")

    if isinstance(single_date, str):
        if single_date != "":
            check_single_date = single_date.split('-')
            
            if len(check_single_date) != 3:
                print("Invalid date provided. YYYY-MM-DD format expected, " + single_date + " given.")
                sys.exit(1)
            if len(check_single_date[0]) != 4:
                print("Invalid date provided. YYYY-MM-DD format expected, " + single_date + " given.")
                sys.exit(1)
            url = url.replace("latest", single_date)
    else:
        print("Unexpected single_date variable type. Str expected, " + str(type(currencies)) + "given.")
        sys.exit(1)

    if print_debug:
        print("\n" + url + "\n")

    response = requests.get(url)

    if response.status_code != 200:
        print("Rates API call failed with status code: " + str(response.status_code) + ".")
        sys.exit(1)
    else:
        if print_debug:
            print("Rates API call was sucesfull." + "\n")

    json_dump = json.dumps(response.json())
    rates_dict = json.loads(json_dump)

    if return_dict:
        if print_debug:
            print(rates_dict)
        return rates_dict
    else:
        if print_debug:
            print(json_dump)
        return json_dump
