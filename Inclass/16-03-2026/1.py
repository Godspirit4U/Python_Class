def target_sum(l, s):
    count = 0
    res = []
    '''Repeating elements are allowed'''
    # for el in l:  
    #     for le in l:
    #         if el + le == s:
    #             count += 1

    '''Repeating elements are not allowed'''
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == s:
    #             count += 1
    #             res.append((l[i], l[j]))
    # return f"\ncount = {count} and the combinations are :-\n {res}"

    ''' Sum of three elements'''
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         for k in range(j+1, len(l)):
    #             if l[i] + l[j] + l[k] == s:
    #                 count += 1
    #                 res.append((l[i], l[j], l[k]))
    # return f"\ncount = {count} and the combinations are :-\n {res}"


l1 = [2, 1, 3, 2, 1, 4, 5]
sum = 5
print(target_sum(l1, sum))
