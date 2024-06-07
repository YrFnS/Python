# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
gcd = 1

for i in range(1, min(a, b)):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)
