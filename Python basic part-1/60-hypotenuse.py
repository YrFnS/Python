# Write a Python program to calculate the hypotenuse of a right angled triangle.

import math

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))

print(math.hypot(a, b))

# h = (x**2 + y**2)**0.5

a = a ** 2
b = b ** 2

print((a + b) ** 0.5)
