num = int(input("Enter a number: "))
sum = 0
org_num = num
while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    sum += fact
    num //= 10

if org_num == sum:
    print("It is a Strong number")
else:
    print("It is not a strong number.")
