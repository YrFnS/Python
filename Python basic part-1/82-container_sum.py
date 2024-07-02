# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

num1 = [1, 2, 2, 4, 87, 0, 4]
num2 = (1, 2, 2, 4, 87, 0, 4)
num3 = {1, 2, 2, 4, 87, 0, 4}
num4 = {'a':1, 'b':2, 'c':2}

print(type(num1), type(num2), type(num3), type(num4))

print(sum(num1), sum(num2), sum(num3), sum(num4.values()))
