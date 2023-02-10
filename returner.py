#!/usr/bin/env python

import sys

# Take input value from the command line
input_value = int(sys.argv[1])

# Check if an argument was passed in
if len(sys.argv) < 2:
    print("Error: No argument passed in")
else:
# Perform calculation on input value
  result = input_value ** 2
  print(result)
