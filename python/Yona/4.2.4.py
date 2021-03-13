import calendar
date = input("Enter a date: ")
day = date[0:2]
month = date[3:5]
year = date[6:10]

day = int(day)
month = int(month)
year = int(year)

week_day = calendar.weekday(year, month, day)

if(week_day == 0):
    print("Monday")
elif(week_day == 1):
    print("Tuesday")
elif(week_day == 2):
    print("Wednesday")
elif(week_day == 3):
    print("Thursday")
elif(week_day == 4):
    print("Friday")
elif(week_day == 5):
    print("Saturday")
else:
    print("Sunday")

