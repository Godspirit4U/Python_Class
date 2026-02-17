'''Write a program that takes as input two integers and checks if their LCM is equal to at least
one of the given integers'''  

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 == 0 or num2 == 0:
    print("LCM is not defined when one of the numbers is zero.")
elif num1 % num2 == 0 or num2 % num1 == 0:
    print("LCM is equal to one of the given numbers.")
else:
    print("LCM is not equal to any of the given numbers.")
