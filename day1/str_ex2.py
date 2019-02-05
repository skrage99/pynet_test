#!/usr/bin/env python

#Create a python script that prompts for an IP address.
#Use #! at top of file; make executable
#split on ‘.’
#Print out four octets with column width of 12; left aligned.
#Check your code into github

ip_address = input("Please enter an IP address:  ")
#print(ip_address)

ip_address = ip_address.split(".")
print()
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_address))
print()

print(ip_address)
