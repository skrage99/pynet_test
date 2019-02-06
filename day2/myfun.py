#!/usr/bin/env python

def my_func(x, y, z=33):
    print(x)
    print(y)
    print(z)

my_dict = {
    'x':1,
    'y':2,
    'z':3,
}
my_func(**my_dict)
