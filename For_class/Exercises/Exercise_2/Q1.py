'''Write a program to swap the contents of two variables using only bitwise operations.'''

a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)