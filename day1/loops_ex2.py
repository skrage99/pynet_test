#!/usr/bin/env python

#Use a while loop and a counter variable i.
#Initialize i to an initial value of 0
#Stay in the while loop until i is greater than 49
#Increment i each time through the while loop
#Print out i (except don't print out i when it is 13).

myloop = 0
while myloop <= 49:
    if myloop == 13:
        myloop += 1
        continue
    print(myloop)
    myloop += 1

