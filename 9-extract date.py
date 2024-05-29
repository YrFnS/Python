import re
from datetime import datetime

happy_day = 'Next month 2020-5-2 is a happy day!'

day = re.search('\d{4}-\d{1}-\d{1}', happy_day)

date = datetime.strptime(day.group(), '%Y-%m-%d').date()

print(date)