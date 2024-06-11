# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

import math

x1 = int(input('Enter the x coordinate of the first point: '))
y1 = int(input('Enter the y coordinate of the first point: '))

x2 = int(input('Enter the x coordinate of the second point: '))
y2 = int(input('Enter the y coordinate of the second point: '))

distance = math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)

print(distance)
