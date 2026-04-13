# 1
'''def countdigits(num):
    if num == 0:
        return 0
    return 1 + countdigits(num//10)


print(countdigits(123456789))'''
# 2
'''def countchars(word):
    if len(word) == 0:
        return 0
    else:
        return 1 + countchars(word[:len(word) - 1])  # i used at ending limit to remove from end like pop. # we an use word[1:] as simple


print(countchars("ABCD"))
'''


# 3
'''def times(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    return a + times(a, b-1)


print(times(12, 0))'''

# 4
# min coins required
'''
def coins(amt):
    if amt == 0:
        return 0
    if amt // 5 > 0:
        return 1 + coins(amt - 5)
    elif amt // 2 > 0:
        return 1 + coins(amt - 2)
    else:
        return 1 + coins(amt - 1)
'''