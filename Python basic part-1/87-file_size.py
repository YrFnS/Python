# Write a Python program to get the size of a file.

import os

file = __file__

print(f'{file} size is {os.path.getsize(file)} bytes')
