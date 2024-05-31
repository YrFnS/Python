import calendar

year = int(input('Enter the year: '))
month = int(input('Enter the month: '))

days = calendar.month(year, month)
print(str(days))
