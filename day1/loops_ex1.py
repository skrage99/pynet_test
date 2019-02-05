#!/usr/bin/env python

#Create a list containing the values 1-49
#Loop over this list, printing each value
#Use continue to skip over 13 (not print it)
#Break when you hit 39 (stop printing after this and exit the loop)

mylist = list(range(49))

for mylist in mylist:
    if mylist == 13:
        continue
    elif mylist == 39:
        break
    print(mylist)


