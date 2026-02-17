# Write a program that takes three integers as input and prints the minimum (of the three
# values).

def min_of_3(a, b, c):
    if a <= b and a <= c:
        print(f'{a} is Minimum')
    elif b <= a and b <= c:
        print(f'{b} is Minimum')
    else:
        print(f'{c} is Minimum')


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
min_of_3(num1, num2, num3)