#!/usr/bin/env python

#create a 3 line file
#Write a python program that reads this file and prints out the lines of t    he file
#write a python program that writes a different file
#close this new file and re-open it and append to it.
#Check your code into GitHub



myfile = open("readme.txt", "r")
contents = myfile.readlines()
print (contents)
myfile.close()

myfile2 = open("create2.txt", "w")
myfile2.write("Sienna Rocks\n")
myfile2.close()


append_file = open("create2.txt", "a")
append_file.write("appended")
append_file.close()

