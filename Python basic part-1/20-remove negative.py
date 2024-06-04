# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
# num = '-6, -4, 5'
# print(num.replace('-', ''))

text = input('Enter a text: ')
num = int(input('Enter number of times to print the copy: '))

print(f'{text} ' * num)
