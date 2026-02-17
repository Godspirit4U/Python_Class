"""Write a program that takes an integer as input and checks, using bitwise operations, if it is
divisible by 4."""

number = int(input("Enter a number: "))

if number & 3 == 0:
    print(True)
else:
    print(False)