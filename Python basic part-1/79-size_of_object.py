# Write a Python program to get the size of an object in bytes.

import sys

class Python:
    def __init__(self):
        self.name = 'Python'
        self.size = sys.getsizeof(self)

python_object = Python()

print(f'Size of Python object in bytes: {python_object.size} bytes')
