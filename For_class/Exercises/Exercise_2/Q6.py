'''Write a program that takes as input two integers and prints appropriate messages if at least
one or both are positive, negative, or zero.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > 0 and num2 > 0:
    print("Both are positive.")
elif num1 < 0 and num2 < 0:
    print("Both are Negative.")

elif num1 == 0 and num2 == 0:
    print("Both are Zeores.")
elif num1 > 0:
    if num2 < 0:
        print("One is Positive and other is Negative.")
    elif num2 == 0:
        print("One is Positive and other is Zero.")
elif num1 < 0:
    if num2 > 0:
        print("One is Negative and other is Positive.")
    elif num2 == 0:
        print("One is Negative and other is Zero.")
elif num1 == 0:
    if num2 < 0:
        print("One is Zero and other is Negative.")
    elif num2 > 0:
        print("One is Zero and other is Positive.")
