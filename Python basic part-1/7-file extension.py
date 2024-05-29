import os

file = input('Enter the file name: ')

extension = os.path.splitext(file)

print(extension[1])