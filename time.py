import datetime as dt

today = dt.date.today()

print('Year: ', today.year)
print('Month: ', today.month)
print('Day: ', today.day)

now = dt.datetime.now()
print(now)