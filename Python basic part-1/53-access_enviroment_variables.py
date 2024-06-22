# Write a Python program to access environment variables.

import os

# print(os.environ)
# print(os.environ['PATH'])
# print(os.environ['HOME'])

for key, value in os.environ.items():
    print(f'{key}: {value}')
