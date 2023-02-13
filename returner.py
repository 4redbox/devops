#!/usr/bin/env python

import sys
input_value = int(sys.argv[1])
    
# Check if an argument was passed in
if len(sys.argv) < 2:
  print('error')  
else:
# Perform calculation on input value

  result = input_value ** 2
  print(result)
