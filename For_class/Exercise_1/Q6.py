# Write a program that takes two integers a and b as input and displays whether a < b, a = b,
# or a > b.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f'{num1} > {num2}')
elif num1 == num2:
    print(f'{num1} = {num2}')
else:
    print(f'{num1} < {num2}')