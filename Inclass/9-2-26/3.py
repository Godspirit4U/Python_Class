string = input("Enter a string: ")
character = input("Enter a character: ")
found = 0
for ch in string:
    if ch == character:
        print(f"The character '{character}' is in the string")
        found = 1
        break

if found == 0:
    print(f"The character '{character}' is not in the string")
