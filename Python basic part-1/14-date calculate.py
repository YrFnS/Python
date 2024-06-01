from datetime import date

# format = 'Y%/%m/%d'

today = date.today()
# another_day = date(int(input('Enter a day format: ')))
another_day = date(2024, 2, 23)

calculate = today - another_day

print(today)
print(calculate.days)
