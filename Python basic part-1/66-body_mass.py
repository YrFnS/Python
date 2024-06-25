# Write a Python program to calculate the body mass index.

weight = float(input('Enter your weight: '))
hight = float(input('Enter your weight: '))

body_mass = weight / (hight / 100) ** 2

print(round(body_mass, 2))
