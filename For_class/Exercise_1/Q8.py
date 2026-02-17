# Write a program that takes a three-digit integer as input and prints the sum of its digits.

number = int(input("Enter a 3 digit number: "))
sum = 0

if number > 99 and number < 1000:
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10

    print(sum)
else:
    print("Invalid input")
