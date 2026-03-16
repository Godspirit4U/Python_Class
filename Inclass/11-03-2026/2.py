''' Write a Python program to take input from the user as list and find the number with highest frequency.'''


def max_freq(counts):
    #  Maximum
    max = counts[0]
    for i in counts:
        if i > max:
            max = i

    for i in range(len(counts)):
        if counts[i] == max:
            print(f"value with maximum frequency is {printed[i] }")
            break

def min_freq(counts):
    #  Maximum
    min = counts[0]
    for i in counts:
        if i < min:
            min = i

    for i in range(len(counts)):
        if counts[i] == min:
            print(f"value with minimum frequency is {printed[i] }")
            break

l1 = list(map(int, input("Enter numbers: ").split()))
print(l1)
printed = []
counts = []
for i in l1:
    count = 0
    for j in l1:
        if i == j:
            count += 1
    
    # print(f"{i} : {count} times")
    printed.append(i)
    counts.append(count)


max_freq(counts)
min_freq(counts)