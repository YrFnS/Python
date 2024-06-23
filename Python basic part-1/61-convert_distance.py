# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

feet = float(input('Enter distance in feet to convert\n'))
inches = feet * 12
yards = feet / 3
miles = feet / 5280

print(f'{feet} feet is {inches} inches, {yards} yards and {miles} miles')
