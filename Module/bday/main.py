import datetime
from bday_messages import random_message

today = datetime.date.today()

month = int(input('When is your birthday month: '))
day = int(input('When is your birthday day: '))
next_birthday = datetime.date(2026, month, day)

days_away = next_birthday - today

if today == next_birthday:
    print(random_message)
else:
    print(f'My next birthday is {days_away} hours away!') 