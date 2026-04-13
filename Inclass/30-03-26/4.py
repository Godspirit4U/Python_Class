def fibbonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    

    if n != 0:
        return fibbonacci(n - 1) + fibbonacci(n - 2)
    
print(fibbonacci(7))

# 0 1 1 2 3 5 8 13