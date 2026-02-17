'''Write a program to check whether a number has 0 as its last digit.'''

number = int(input("Enter a number: "))
if number % 10 == 0:
    print("The last digit is zero")
else:
    print("The last digit is not zero")