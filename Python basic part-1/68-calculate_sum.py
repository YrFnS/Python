# Write a Python program to calculate sum of digits of a number.

num = int(input('Enter a number: '))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(sum)
