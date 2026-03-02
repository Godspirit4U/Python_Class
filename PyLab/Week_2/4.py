n = int(input("Enter how many numbers: "))

max_sum = 0
max_number = 0

for i in range(n):
    num = int(input("Enter number: "))
    temp = num
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_number = num

print("Number with maximum digit sum:", max_number)