# Write a Python program to convert height (in feet and inches) to centimeters.

inch = float(input('Enter inch to convert to cm\n'))
feet = float(input('Enter feet to convert to cm\n'))

# i_cm = inch * 2.54
# f_cm = feet * 30.48

# print(f'{inch} inch = {i_cm} cm')
# print(f'{feet} feet = {f_cm} cm')

cm = (feet * 12) * 2.54
cm = cm + inch * 2.54

print(f'{cm} cm')
