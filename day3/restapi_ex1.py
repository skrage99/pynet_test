#!/usr/bin/env python


#Using the Python requests library. Connect to the following URL
#(https://netbox.lasthop.io/api) and retrieve the information there using an
#HTTP GET.

#You will probably need the following HTTP Headers:

#http_headers = {"accept": "application/json; version=2.4;"}




import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    url = "https://netbox.lasthop.io/api/"
    http_headers = {"accept": "application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)
    response = response.json()

    print()
    pprint(response)
    print()
