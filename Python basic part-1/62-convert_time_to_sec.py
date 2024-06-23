# Write a Python program to convert all units of time into seconds.

day = int(input('Enter day: '))
hour = int(input('Enter day: '))
min = int(input('Enter day: '))
sec = int(input('Enter day: '))

day = day * 24 * 60 * 60
hour = hour * 60 * 60
min = min * 60

print(day + hour + min + sec)
