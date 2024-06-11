# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))

# if a == b or (a + b) == 5 or abs(a - b) == 5:
#     print(True)
# else:
#     print(False)


def num(a, b):
     if a == b or abs(a - b) == 5 or (a + b) == 5:
        return True
     else:
        return False
print(num(7, 4))
print(num(7, 7))
print(num(1, 4))
print(num(2, 9))
print(num(5, 4))
