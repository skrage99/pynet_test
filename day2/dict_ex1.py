#!/usr/bin/env python

#Create a dictionary representing a network device
#Assign it an ip address, a username, a password, a vendor, and a mode field.
#Loop over this dictionary printing out all of the keys, and values
#Update the password to be a new value
#Add a secret field to the dictionary
#Use the .get() method to try to retrieve a non-existent ‘device_type’ 
#field. Return a default value of ‘cisco_ios’ when the .get() key lookup fails.


#Create the dictionary "ubiquiti" and populate with vaules 
print("Creating the dictionary 'ubiquiti'")
ubiquiti = {}
ubiquiti['ip_address'] = '10.20.40.90'
ubiquiti['user_id'] = 'shaun'
ubiquiti['password'] = 'doctorpepper'
ubiquiti['vendor'] = 'ubiquiti'
ubiquiti['mode'] = 'enable'

print("Print the key and vaules from the dictionary")
for i,j in ubiquiti.items():
    print("{} .....> {}".format(i,j))

print("")

#Adding a new key/value pair to the ubiquiti dictionary 
print("Adding a new key and vaule to dictionary")
ubiquiti["secret"] = 's3cret'

print("")
device_type = ubiquiti.get("device_type", "cisco_ios")
print("\nDefault device type: {}\n".format(device_type))

print("")

print(device_type)
