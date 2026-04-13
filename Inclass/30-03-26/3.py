def multiply(a, b):
    if b == 0:
        return 0
    
    a += a
    b -= 1

    if b >= 0:
        return multiply(a, b)
    return a


a = int(input("enter: "))
b = int(input("enter: "))

print(multiply(a, b))
