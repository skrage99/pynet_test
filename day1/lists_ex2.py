#!/usr/bin/env python

#Go back to exercise splitting on IP address
#Convert that code to save the split as a list
#Set the last octet of the list to have a ‘0’ value
#Convert each octet to a binary number
#Print out each octet in both decimal and binary

ipaddr = input("Please an IP: ")
myip = ipaddr.split(".")
myip[-1] = 0
print(myip)

ip_bin = []
ip_bin.append(bin(int(myip[0])))
ip_bin.append(bin(int(myip[1])))
ip_bin.append(bin(int(myip[2])))
ip_bin.append(bin(int(myip[3])))

print()
print("{:<12} {:<12} {:<12} {:<12}".format("octet1", "octet2", "octet3", "octet4"))
print("{:<12} {:<12} {:<12} {:<12}".format(*myip))
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_bin))
print()

