l = [0, 1, 2]
# l1 = l
print(l)

l1 = []
for item in l:
    l1.append(item)

l1.append(90)
print(l1)
print(l)

l2 = [ 33, 54 , 4]
l3 = l2[:]
l3.append(5555)
print(l3)
print(l2)