s = input("Enter string: ")

printed = ""

for i in range(len(s)):

    skip = False
    for k in range(len(printed)):
        if s[i] == printed[k]:
            skip = True
            break

    if skip == False:
        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count = count + 1

        print(f"{s[i]} : {count}")
        printed = printed + s[i]
