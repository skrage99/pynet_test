#!/usr/bin/env python

#Netmiko Ex1
#Write a Netmiko script that connects to one Cisco router and one Juniper SRX.
#a. Print the current prompt
#b. use send_command to retrieve 'show version' from the two devices.
#c. use send_command to retrieve running configuration from the two devices.
#d. Save the running config to a file.
#Dictionary for network devices that can be used with Netmiko.
#
#    cisco3 = {
#        'device_type': 'cisco_ios',
#        'host':   'cisco3.lasthop.io',
#        'username': 'pyclass',
#        'password': getpass(),
#    }
#
#    srx2 = {
#        'device_type': 'juniper_junos',
#        'host':   'srx2.lasthop.io',
#        'username': 'pyclass',
#        'password': getpass(),
#    }


from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler

def save_file(filename, show_run):
    with open(filename, "w") as f:
        f.write(show_run)


def main():
    password = getpass("88newclass")
    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    srx2 = {
        "device_type": "juniper_junos",
        "host": "srx2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    for a_device in (cisco3, srx2):
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        show_ver = net_connect.send_command("show version")
        print()
        print("#" * 80)
        print(show_ver)
        print("#" * 80)
        print()

        if "cisco" in a_device["device_type"]:
            cmd = "show run"
        elif "juniper" in a_device["device_type"]:
            cmd = "show configuration"

        show_run = net_connect.send_command(cmd)
        filename = net_connect.base_prompt + ".txt"
        print("Save show run output: {}\n".format(filename))
        save_file(filename, show_run)



