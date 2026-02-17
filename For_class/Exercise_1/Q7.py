# Write a program that takes three integers as input and prints their maximum value.

def max_of_3(a, b, c):
    if a >= b and a >= c:
        print(f'{a} is Maximum')
    elif b >= a and b >= c:
        print(f'{b} is Maximum')
    else:
        print(f'{c} is Maximum')


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
max_of_3(num1, num2, num3)