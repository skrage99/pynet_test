#!/usr/bin/env python



#Functions Ex2
#--------------
#
#Expand on functions exercise 1.
#
#a. Create a list with three numbers
#b. Use *args to call the function
#c. Create a dictionary that has three keys of x, y, and z
#d. Call the functions using **kwargs

#Define function called "jake"
def jake(a, b, c):
    return a + b + c

#Create list with 3 numbers, assigned to rhel_versions variable 
rhel_versions = [5, 6, 7]
print ("What is the variable now?  ")
print (rhel_versions)
return_val = jake(*rhel_versions)
print("Return value of my list: {}".format(return_val))

#Create a dictionary called webster and assign values to a, b, and c
webster = {"a": 100, "b": 200, "c": 300}
return_val = jake(**webster)
print("Return value of webster dictionary:{}".format(return_val))
