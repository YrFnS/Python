# Write a Python program to check whether lowercase letters exist in a string.

text = "hello world"

x = any(text.islower() for x in text)

print(x)
