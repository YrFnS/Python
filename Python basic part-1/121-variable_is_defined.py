# Write a Python program to determine if a variable is defined or not

try:
    value
    print('Defined')
except NameError:
    print('Not defined')
