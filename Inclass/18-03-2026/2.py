s = input("Enter string: ")
length = len(s)
k = int(input("Enter length to divide string: "))
if length % k != 0:
    print("Invalid division of string!")
    exit

i = 0
l1 = []
l2 = []
for c in range(length // k):
    temp = s[i+(k *c) : k+(k*c) : ]
    l1.append(temp)

print(l1)
for sub in l1:
    temp1 = ''
    for ch in sub:
        if ch not in temp1:
            temp1 += ch
    if temp1 not in l2:
        l2.append(temp1)
print(l2)

# def merge_the_tools(string, k):
#     # your code goes here
#     i = 0
#     for c in range(len(string) // k):
#         temp = string[k * c: k+(k*c)]
#         temp1 = ''
#         for ch in temp:
#             if ch not in temp1:
#                 temp1 += ch
#         print(temp1)


# string, k = input(), int(input())
# merge_the_tools(string, k)
