#!/usr/bin/env python

#Functions Ex3
#--------------

#Based on your earlier exercise where you parsed the serial number from
# show_version

#a. Create two functions
#b. Function1 opens the file and returns all of the data in the file as a text
#   string. This function should take one argument (the filename).
#c. Function2 parses the show_version output and returns the serial number

# Create function to read the file. 
def readthefile(var_config):
    with open (var_config) as f:
        return f.read()


# Create function to find serial number
def find_serial_number(show_ver):
    serial_number = ""
    for line in show_ver.splitlines():
        if "Processor board ID" in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number



#Opens show_version.txt and displays to the screen
filename="show_version.txt"
output=readthefile(filename)
print(output)

#Opens show_version.txt and returns the serial number 
my_file = "show_version.txt"
show_ver = readthefile(my_file)
serial_number = find_serial_number(show_ver)
print("\nSerial Number is {}\n".format(serial_number))

