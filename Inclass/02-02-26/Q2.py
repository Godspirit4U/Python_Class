''' Using bitwise operator tell that a number is divisible by 4 or not'''

num = int(input("Enter a positive integer: "))
if num & 3 == 0:
    print("It is divisible by 4")
else:
    print("It is not divisible by 4")

if num & 7 == 0:
    print("it is divisible by 8")
else:
    print("Not by 8")