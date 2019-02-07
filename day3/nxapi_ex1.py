#Connect to nxos2 using NX-API and JSON-RPC
#Retrieve 'show version' from this device.
#From this 'show version' output extract the device's serial number.


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show version")
serial_number = output["proc_board_id"]
print()
print(serial_number)
print()

