#!/usr/bin/env python

# Create a YAML dictionary in a file. Use Python to read it and print it to the screen. The
# dictionary should have at least four keys; one of the values in the dictionary should be a list.

import yaml
from pprint import pprint

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)


filename = "stuff.yml"
pprint(read_yaml(filename))

