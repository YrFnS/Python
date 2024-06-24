# Write a Python program that converts seconds into days, hours, minutes, and seconds.

sec = int(input('Enter the number of seconds: '))

day = sec // 86400
r_sec = sec % 86400
hour = r_sec // 3600
min = hour % 60
sec = r_sec % 60

print(f'{day} days, {hour} hours, {min} minutes, {sec} seconds')
