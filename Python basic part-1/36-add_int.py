# Write a Python program to add two objects if both objects are integers.

def num(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return False
    else:
        return a + b

print(num(4, 5))
print(num('e', 4))
print(num(8.9, 8))
print(num(3, '4'))
print(num('4.5', 4.2))
