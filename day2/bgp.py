#!/usr/bin/env python

filename = "show_ip_bgp.txt"
with open(filename, "r") as f:
    bgp_table = f.read()

fields = bgp_table.split("Weight Path")
bgp_table = fields[1]

bgp_list = bgp_table.splitlines()

for line in bgp_table.splitlines():
    if not line.strip():
        continue
    fields = line.split()
    prefix = fields[1]
    #print(prefix)
    #print(fields[5])
    as_path = fields[5:-1]
    print(as_path)
    print("{:30}{:50}".format(prefix, str(as_path)))

    #print(repr(line))
    #break

