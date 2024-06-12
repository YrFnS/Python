# Write a Python program to check whether a file exists.

import os

file = 'path/my/app.js'

if os.path.exists(file):
    print('File exists')
else:
    print('File does not exist')
