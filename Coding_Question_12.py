import datetime
year, month, day = map(int, input().split(","))
print(datetime.date(year, month, day).isocalendar()[1])
