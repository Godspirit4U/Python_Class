word = input("Enter a 4-letter word: ")

result = ""

for ch in word:
    result += chr(ord(ch) ^ 32)

print("Toggled word:", result)
