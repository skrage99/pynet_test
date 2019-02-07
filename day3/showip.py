#!/usr/bin/env python
import re
from pprint import pprint 
filename = "show_ip_int_brief.txt"

with open(filename) as some_var:
    show_ip_int = some_var.read()

show_ip_int = show_ip_int.strip()

output_dict = {}
for line in show_ip_int.splitlines():
    if 'Interface' in line:
        continue
    fields = line.split()
    interface = fields[0]
    ipaddress = fields[1]
    linestatus = fields[4]
    lineprotocol = fields[5]
    output_dict[interface] = {} 
    output_dict[interface]["ipaddress"] = ipaddress
    output_dict[interface]["linestatus"] = linestatus
    output_dict[interface]["lineprotocol"] = lineprotocol
    print(output_dict)



pprint(output_dict)






