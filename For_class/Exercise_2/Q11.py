'''Write a program that takes a date in the format DDMMYYYY and prints the day of the week it
falls on. Given: 01-01-1990 was a Monday.'''


def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


# Take input date
DDMMYYYY = input("Enter the date: ")
date = int(DDMMYYYY[0:2])
month = int(DDMMYYYY[2:4])
year = int(DDMMYYYY[4:])

# imp lists
week_days = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total_days = 0
# count no of days wrt years
if year >= 1990:
    for i in range(1990, year):
        if is_leap(i):
            total_days += 366
        else:
            total_days += 365
else:
    for i in range(1989, year-1, -1):
        if is_leap(i):
            total_days += 366
        else:
            total_days += 365


# count no of days wrt months

# choose month days
month_days = leap_year_days if is_leap(year) else year_days
if year > 1990:
    for m in range(month - 1):
        total_days += month_days[m-1]
    total_days += date - 1
else:
    for m in range(month - 1, 12):
        total_days -= month_days[m]
    total_days = month_days[month - 1] - date + 1

day_index = total_days % 7
print(week_days[day_index])