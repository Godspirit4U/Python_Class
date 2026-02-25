'''Write a program that takes a 4-character binary number and prints its decimal equivalent.
Note: Do not use hex, bin, or int functions.'''

binary = input("Enter a 4-character binary number: ")
decimal = 0
power = 3

for num in binary:
    if num == '1':
        decimal += 2 ** power
    power -= 1

print("Decimal equivalent:", decimal)