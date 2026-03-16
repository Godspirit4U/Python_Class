l1 = list(map(int, input("enter numbers: ").split(" ")))
print(l1)

l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)