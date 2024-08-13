# Write a Python program to list the home directory without an absolute path.

import os

home_dir = os.path.expanduser('~')
print(home_dir)
