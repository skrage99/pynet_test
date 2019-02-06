#!/usr/bin/env python

#Functions Ex1
#--------------

#a. Construct a function that has three parameters x, y, z
#b. z has a default value of 20
#c. Return x + y + z
#d. Call this function using all three positional arguments
#e. Call this function using named arguments x, y (let z be the default)
#f. Call this function with one positional argument and two named arguments.
#g. Call this function using three strings.
#h. Call this function using three lists.

def fn(x, y, z=20):
    return x + y + z

fn_val = fn(10, 15, 20)

return_val = fn(x=10, y=20)
print("Calling with two named args: {}".format(return_val))

return_val = fn(100, z=15, y=20)
print("Calling with 1 pos arg and two named args: {}".format(return_val))

return_val = fn(x="x_wife", y="y_bother", z="zebra")
print("Calling 3 strings assigned to x, y, and z: {}".format(return_val))

return_val = fn(x=["xtra"], y=["years"], z=["zany"])
print("Call function with three lists: {}".format(return_val))
print()

