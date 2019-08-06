# pyrates
Small &amp; Easy-to-use Python module for getting currency rates from live API.
It provides rates for one, multiple or all currencies with the possibility to change the base currency and get the historical rates. 

The return value is either `json` or python dictionary. 

# Installation:
Git clone this repository and import `get_rates` method to your `.py` file like so:
```from pyrates import get_rates``` (`pyrates.py` file is in this case in the same folder as your `.py` file)

# Use:
`get_rates` function has the following input parameters (and their expected types):
  - base_currency (str) - select base currency for conversion; EUR by default
  - currencies (str or list) - currency/list of currencies to get rates for; all by default
  - single_date (str) - date for which the rates should be provided (`YYYY-MM-DD` format expected; current date by default
  - date_interval (list) - interval for which the rates should be provided (list of two values in the same format as for single date expected); empty by default and has priority if used together with `single_date` parameter
  - print_debug (boolean) - prints debug description for easier debugging - this description contains API request url, api status code and more; False by default
  - return_dict (boolean) - determines if dictionary or json should be returned. If `True` dictionary, if `False` json is returned; `True` by default  

