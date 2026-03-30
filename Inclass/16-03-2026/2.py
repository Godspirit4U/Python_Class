# name = "Yagami"
# print(name[::-1])

# def long_sub_seq(l):
#     res = []
#     for i in range(len(l)):
#         ss = 1
#         for j in range(i+1, len(l)):
#             if l[i] < l[j]:
#                 ss += 1
#             else:
#                 break
#         res.append(ss)
#     return max(res)

def long_sub_seq(l):
    res = []
    subs = []
    for i in range(len(l)):
        ss = 1
        temp = [l[i]]
        for j in range(i+1, len(l)):
            if l[i] < l[j]:
                ss += 1
                temp.append(l[j])
            else:
                break
        res.append(ss)
        subs.append(temp)

        max = subs[0]
        for i in range(1, len(subs)):
            if len(subs[i]) > len(max):
                max = subs[i]

    return f"Longest sub string is {max}"


# l = [2, 1, 3, 4, 0, 5]
l = [5, 1, 3, 1, 0, 1, 7]
print(long_sub_seq(l))
