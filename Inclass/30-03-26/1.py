# l = [i for i in range(0, 5)]
# print(l)

# l1 = [i*i for i in range(7)]
# print(l1)

# l2 = [i for i in range(0, 10) if i % 2 == 0]
# print(l2)

# d1 = {i: i*i for i in range(7)}
# print(d1)

# d2 = {i: chr(i) for i in range(65, 80)}
# print(d2)

# t1 = ()
# t1 = 1, 2
# print(t1)

# t3 = (2,3,5,[])
# t3[3].append(123)
# print(t3)

# t4 = tuple(input("").split())
# print(t4)

t = (3, 1, 4, 2, 42, 52, 14)
t = list(t)

for i in range(len(t) - 1):
    for j in range(len(t) - 1):
        if t[j] > t[j+1]:
            t[j], t[j+1] = t[j+1], t[j]
print(tuple(t))
