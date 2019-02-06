#!/usr/bin/env python
# RegEx Ex1
#Use the 'show interface fa4' output (in the file 'show_int_fa4.txt').
#Use regular expressions extract the following:
# packets input/output
#bytes input/output


import re

#Open the file
with open("show_int_fa4.txt") as f:
    output = f.read()
    print(output)

patterns = {
    "Input": r"(\d+) packets input, (\d+) bytes",
    "Output": r"(\d+) packets output, (\d+) bytes",
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print("\n{}: ".format(label))
        print("Packets: {}".format(match.group(1)))
        print("Bytes: {}\n".format(match.group(2)))

