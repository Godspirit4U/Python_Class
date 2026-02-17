s = "saiuniversity"
vowel_count = 0
consonant_count = 0
for i in s:
    if (i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u'):
        vowel_count += 1
    else:
        consonant_count += 1

print(f"vowel count is {vowel_count}")
print(f"consonant count is {consonant_count}")