# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys

script_name = sys.argv[0]
num_arguments = len(sys.argv) - 1
arguments = sys.argv[1:]

print(f'Script name: {script_name}')
print(f'Number of arguments: {num_arguments}')
print(f'Arguments: {arguments}')
