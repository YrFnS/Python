first_name = input('Enter your first name: ')
last_name = input('Your last name: ')

full_name = str(first_name + ' ' + last_name)[::-1]

print(full_name)