def find_common_elements(t1, t2):
    result = []
    for el in t1:
        if el in t2:
            result.append(el)
    return tuple(result)


print(find_common_elements((1, 2, 3, 4, 5), (3, 4, 5, 6, 7)))
