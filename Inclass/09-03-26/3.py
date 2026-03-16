# l = [2,3,5, "Spirit",2,4, [9,8,7]]
# for i in range(len(l) - 1, -1, -1):
#     print(l[i])

# for i in l:
#     print(i)


# for i in l[3]:
#     print(i)


l1 = list(map(int, input("enter numbers: ").split(" ")))
print(l1)

max = min = l1[0]
sum = 0


for i in l1:

    sum += i

    if i > max:
        max = i

    if i < min:
        min = i
average = sum / 10
print(max)
print(min)
print(average)


secmax = l1[0]
for i in l1:
    if i > secmax and i != max:
        secmax = i

print(secmax)