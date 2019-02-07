#!/usr/bin/env python

# Create a YAML list in a file.
# Use Python to read it and print it to the screen. The list should have at least four elements.

import yaml
f = open("hostnames.yml")
output = yaml.load(f)
print(output)
