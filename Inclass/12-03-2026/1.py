d1 = {
    "A": ["B", "D", "E"],
    "B": ["A"],
    "C": ["B", "E"],
    "D": ["C", "A"],
    "E": ["C", "A"]
}


n1 = input("Enter first node: ")
n2 = input("Enter second node: ")

'''if n1 in d1.keys():
    if n2 in d1[n1]:
        print(True)
    else:
        print(False)
else:
    print("Invalid input!")'''


found = False
if n1 in d1.keys():
    for ch in d1[n1]:
        if ch == n2:
            found = True
            break
        else:
            for ch in d1[n1]:
                if n2 in d1[ch]:
                    found = True
                    break
                else:
                    continue

if found:
    print("Found")
else:
    print("NOt found")
