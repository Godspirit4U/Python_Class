def anagrams(s, p):
    result = []
    for i in range(len(s)):
        if sorted(s[i:i+len(p)]) == sorted(p):
            result.append(i)
    return result

def grams(s, p):
    return [i for i in range(len(s)) if sorted(s[i:i+len(p)]) == sorted(p)]


print(anagrams("cbaebabacd", "abc"))
print(grams("cbaebabacd", "abc"))