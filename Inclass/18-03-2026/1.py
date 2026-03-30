s = input("Enter  string: ")
s1 = input("Enter sub string: ")

count = 0
for i in range(len(s)-len(s1)+1):
    temp = ''
    for j in range(len(s1)):
        temp += s[i+j]
    if temp == s1:
        count += 1
print(count)