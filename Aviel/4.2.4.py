import calendar
date = input("Enter a date: ")
day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])
print(calendar.day_name[calendar.weekday(year, month, day)])