# Write a Python program to filter positive numbers from a list.

nums = [1, -4, -8, 78, 25, -53]

print(list(filter(lambda i: i > 0, nums)))

for i in nums:
    if i > 0:
        print(i, end=' ')
