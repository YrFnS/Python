# Write a Python program to retrieve the path and name of the file currently being executed.

import os

# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
print(os.path.realpath(__file__))
