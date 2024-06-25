# Write a Python program to sort files by date.

import os
import time

files = os.listdir()
files.sort(key=lambda x: time.ctime(os.path.getmtime(x)))

for file in files:
    print(file)
