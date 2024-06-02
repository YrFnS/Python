def range(n):
    return abs(1000 - n) <= 100 or abs(2000 - n) <= 100

num = range(int(input('Enter a number: ')))
print(num)
