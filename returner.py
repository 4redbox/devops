#!/usr/bin/env python

import sys
    
# Check if an argument was passed in
if len(sys.argv) < 2:
  print('no input')
else:
# Perform calculation on input value
  input_value = int(sys.argv[1])
  result = input_value ** 2
  print(result)
