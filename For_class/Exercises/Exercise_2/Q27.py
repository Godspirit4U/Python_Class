hex_num = input("Enter a 4-character hexadecimal number: ").upper()

decimal = 0
power = 3

for ch in hex_num:

    if ch == '0':
        value = 0
    elif ch == '1':
        value = 1
    elif ch == '2':
        value = 2
    elif ch == '3':
        value = 3
    elif ch == '4':
        value = 4
    elif ch == '5':
        value = 5
    elif ch == '6':
        value = 6
    elif ch == '7':
        value = 7
    elif ch == '8':
        value = 8
    elif ch == '9':
        value = 9
    elif ch == 'A':
        value = 10
    elif ch == 'B':
        value = 11
    elif ch == 'C':
        value = 12
    elif ch == 'D':
        value = 13
    elif ch == 'E':
        value = 14
    elif ch == 'F':
        value = 15

    decimal += value * (16 ** power)
    power -= 1
else:
    print("Decimal equivalent:", decimal)
