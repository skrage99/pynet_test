#!/usr/bin/env python

mylist = ['who', 'let', 'the', 'dogs', 'out']
mylist.append('owen')
mylist.append('did')
outtoscreen = mylist[:]
print(outtoscreen)
print("Now to remove 'who'")

oneitem = mylist.pop(0)
print(oneitem)

print("Length of list: {}".format(len(mylist)))
mylist.sort()
print(mylist)

