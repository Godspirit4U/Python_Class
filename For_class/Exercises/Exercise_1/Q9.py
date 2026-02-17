# Write a program that takes the marks for 5 subjects as input and calculates the total and
# average marks.

marks = input("Enter: ")
marksof5 = marks.split()
length = len(marksof5)
sum = 0
if length == 5:
    for i in range(5):
        marksof5[i] = int(marksof5[i])
        sum += marksof5[i]
    print(f'sum = {sum}')
    print("Average = ", sum / 5)
else:
    print("Enter 5 subjects marks")