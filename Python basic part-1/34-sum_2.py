# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
    
print(sum(a, b))
