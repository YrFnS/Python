# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2

text = input('Enter text to print: ')
num = int(input('How many copies of the string you need: '))

print(f'{text[:2]} ' * num)
