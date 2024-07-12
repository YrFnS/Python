# Write a Python program to extract the filename from a given path.

import os

path = __file__
filename = os.path.basename(path)

print(filename)
