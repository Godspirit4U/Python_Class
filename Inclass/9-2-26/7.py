s = "Sai"
for i in range(0,9):
    try:
        print(s[i])
    except IndexError:
        continue