# Write a Python program to prove that two string variables of the same value point to the same memory location.

a = 'Python'
b = 'Python'

print(id(a) == id(b))
print(id(a))
print(id(b))
