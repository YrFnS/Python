# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

nums = [1, 8, 84, 151, 101, 684, 15, 579, 158, 7896, 45, 68, 76, 18, 68, 46, 30]

num = filter(lambda n: n % 15 == 0, nums)

print(list(sorted(num)))
