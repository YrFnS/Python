# Write a Python program that inputs a number and generates an error message if it is not a number.

num = input("Input a number: ")

try:
    print(int(num))
except:
    print('Not a number')
