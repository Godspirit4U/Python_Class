def seperate(word):
    s = []

    for ch in word:
        found = False
        for i in range(len(s)):
            if ch in s[i]:
                s[i] += ch
                found = True
                break
        if found == False:
            s += [ch]
    return s


print(seperate('cartoon'))
print(seperate('network'))
print(seperate('aabbcc'))
print(seperate('cccbbaaaccc'))
