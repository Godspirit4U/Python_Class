def product(l):
    res = []
    for i in range(len(l)):
        temp = 1
        for j in range(len(l)):
            if i != j:
                temp *= l[j]
        res.append(temp)
    return res


print(product([1, 2, 3, 4]))
