def LLS(s):
    res = 0
    for i in range(len(s)):
        temp = ""
        for j in range(i, len(s)):
            if s[j] not in temp:
                temp += s[j]
        if len(temp) > res:
            res = len(temp)
    return res

print(LLS("abcabcbb"))
print(LLS("bbbbb"))