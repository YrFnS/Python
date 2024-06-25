# Write a Python program to sort three integers without using conditional statements and loops.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

num1 = min(a, b, c)
num2 = max(a, b, c)
num3 = (a + b + c) - num1 - num2

print(num1, num3, num2)
