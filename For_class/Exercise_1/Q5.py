# Write a program that takes an integer as input, and displays whether this integer is negative,
# positive, or zero.

num = int(input("Enter a number:n "))

if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")