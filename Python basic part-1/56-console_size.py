# Write a Python program to get the height and width of the console window.

import os

print(os.get_terminal_size())

height, width = os.get_terminal_size()

print(f'Height: {height}\nWidth: {width}')
