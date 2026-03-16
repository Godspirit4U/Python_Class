d1 = {}

l1 = list(map(int, input("Enter numbers: ").split()))

for i in l1:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1

key = i
for i in d1.keys():
    if d1[i] > d1[key]:
        k = i

print(f"{key} occured {d1[key]} times")