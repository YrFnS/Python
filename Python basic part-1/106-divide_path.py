# Write a Python program to divide a path by the extension separator.

import os.path

path = '/Python basic part-1/106-divide_path.py'

root, ext = os.path.splitext(path)

print('Root =', root)
print('Extension =', ext)
