# Write a Python program to find the least common multiple (LCM) of two positive integers.
import math

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

def lcm(x, y):
    while(y):
        x, y = y, x % y
    return x
lcm = (a * b) // lcm(a, b)

print(lcm)
print(math.lcm(a, b))
