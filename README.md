# pyrates
Small &amp; Easy-to-use Python module for getting currency rates from live API.
It provides rates for one, multiple or all currencies with the possibility to change the base currency and get the historical rates. 

The return value is either `json` or python dictionary. 

# Installation:
Git clone this repository and import `get_rates` method to your `.py` file like so:
```from pyrates import get_rates``` (`pyrates.py` file is in this case in the same folder as your `.py` file)

# Requirements:
Python3 + requests module (howto: https://2.python-requests.org/en/master/user/install/)

# Use:
`get_rates` function has the following input parameters (and their expected types):
  - base_currency (str) - select base currency for conversion; EUR by default
  - currencies (str or list) - currency/list of currencies to get rates for; all by default
  - single_date (str) - date for which the rates should be provided (`YYYY-MM-DD` format expected; current date by default
  - [WIP - not implemented yet] date_interval (list) - interval for which the rates should be provided (list of two values in the same format as for single date expected); empty by default and has priority if used together with `single_date` parameter
  - print_debug (boolean) - prints debug description for easier debugging - this description contains API request url, api status code and more; False by default
  - return_dict (boolean) - determines if dictionary or json should be returned. If `True` dictionary, if `False` json is returned; `True` by default  

# Examples:
1. Get all currencies rates as dictionary:
code (with import):
```
#!/usr/bin/env python3

from pyrates import get_rates

dict = get_rates()
```
output:
```
{
'rates': 
  {'CAD': 1.4785,
  'HKD': 8.767,
  'ISK': 136.5, 
  'PHP': 58.269,
  'DKK': 7.4644,
  'HUF': 325.35,
  'CZK': 25.727,
  'AUD': 1.6467,
  'RON': 4.73,
  'SEK': 10.7267,
  'IDR': 15958.26,
  'INR': 79.215,
  'BRL': 4.4099,
  'RUB': 72.7977,
  'HRK': 7.384,
  'JPY': 119.1,
  'THB': 34.394,
  'CHF': 1.0919,
  'SGD': 1.5441,
  'PLN': 4.3119,
  'BGN': 1.9558,
  'TRY': 6.1906,
  'CNY': 7.8521,
  'NOK': 9.9545,
  'NZD': 1.7073,
  'ZAR': 16.5635,
  'USD': 1.1187,
  'MXN': 21.8702,
  'ILS': 3.9088,
  'GBP': 0.9183,
  'KRW': 1357.32,
  'MYR': 4.684},
'base': 'EUR',
'date': '2019-08-06'
}
```

2. Get some currencies rates as dictionary:
code:
  ```
  dict = get_rates(currencies = ["usd", "chf", "gbp"])
  ```
output:
```
{
'rates': 
  {'CHF': 1.0919,
   'USD': 1.1187,
   'GBP': 0.9183},
 'base': 'EUR',
 'date': '2019-08-06'
}
```

3. Get some rates as json with base currency USD:
code:
```
json = get_rates(base_currency = "usd", currencies = ["eur", "chf", "gbp"], return_dict = False)
```
output:
```
{
   "rates":{
      "CHF":0.9760436221,
      "EUR":0.8938946992,
      "GBP":0.8208635023
   },
   "base":"USD",
   "date":"2019-08-06"
}
```

3. Get some rates as json with base currency USD and single date set to `2019-05-22`:
code:
```
dict = get_rates(
  base_currency = "usd",
  currencies = ["eur", "chf", "gbp"],
  single_date = "2019-05-22", 
  return_dict = False
)

```
output:
```
{
   "rates":{
      "CHF":1.0072509176,
      "EUR":0.8951750067,
      "GBP":0.7902604959
   },
   "base":"USD",
   "date":"2019-05-22"
}
```

4. Get some rates as json with base currency USD and single date set to `2019-05-22` and debug description:
code:
```
json = get_rates(
  base_currency = "usd",
  currencies = ["eur", "chf", "gbp"],
  single_date = "2019-05-22",
  print_debug = True,
  return_dict = False
)
```
console-printed output:
```
https://api.exchangeratesapi.io/2019-05-22?base=USD&symbols=EUR,CHF,GBP

Rates API call was sucesfull.

{
   "rates":{
      "CHF":1.0072509176,
      "EUR":0.8951750067,
      "GBP":0.7902604959
   },
   "base":"USD",
   "date":"2019-05-22"
}
```
