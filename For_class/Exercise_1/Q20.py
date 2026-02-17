"""Write a program that takes a character as input and prints the alpha-numeric character (0–9,
A–Z, a–z are alpha-numeric characters) that is closest to this character.
Note: If the input character is equidistant from two alpha-numeric values, either one can
be printed.
"""
character = input("Enter a character")
if len(character) == 1:

    ascii = ord(character)
    if ascii < 48:
        print(chr(48))
    elif (ascii >= 48 and ascii <= 57) or (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        print(character)
        '''we can also use character.isalnum()'''
    elif ascii > 57 and ascii < 65:
        d1 = abs(ascii - 57)
        d2 = abs(ascii - 65)
        if d1 > d2:
            print(chr(65))
        else:
            print(chr(57))
    elif ascii > 90 and ascii < 97:
        d1 = abs(ascii - 90)
        d2 = abs(ascii - 97)
        if d1 > d2:
            print(chr(97))
        else:
            print(chr(90))
    elif ascii > 122 and ascii < 128:
        print(chr(122))
    else:
        print("Invalid Input!")
else:
    print("Enter only single character!")