n = int(input("Enter how many numbers: "))

even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Even Sum =", even_sum)
print("Odd Sum =", odd_sum)
