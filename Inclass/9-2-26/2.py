s = "saiUN  IVErsity"
s1 = ""
for i in s:
    if ord(i) <= 122 and ord(i) >= 97:
        s1 += chr((ord(i) - 32))
    else:
        s1 += i
print(s1)
