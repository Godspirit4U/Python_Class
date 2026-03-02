s = input("Enter sentence: ")
if s == "":
    print(0)
else:
    count = 1
    for ch in s:
        if ch == " ":
            count += 1

    print("Words =", count)