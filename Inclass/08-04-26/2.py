def revTuple(t):
    t = list(t)
    t = tuple(t[::-1])
    return t



t1 = (1, 2, 3)

t1 = revTuple(t1)
print(t1)
