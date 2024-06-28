# Write a Python program to get a directory listing, sorted by creation date.

import os

files = os.listdir()
files.sort(key=lambda f: os.path.getctime(f))

print(files)
