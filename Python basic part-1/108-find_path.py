# Write a Python program to find the path to a file or directory when you encounter a path name.

import os

print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(os.getcwd())
print(os.path.realpath(__file__))
print(os.path.dirname(__file__))
print(os.path.isfile(__file__))
print(os.path.isdir(__file__))
print(os.path.join(__file__))
