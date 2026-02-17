'''Write a program that takes a year as input and prints whether it is a leap year or not. Note:
The year can be any year in the past or up to 100 years into the future.'''

year = int(input("Enter the year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("It is a leap year")
else:
    print("It is not a leap year")
