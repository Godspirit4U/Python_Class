# Write a program that takes a floating-point value as input and prints its absolute value.

num = float(input("Enter a floating-point number: "))

if num < 0:
    num = -num

print("Absolute value =", num)
