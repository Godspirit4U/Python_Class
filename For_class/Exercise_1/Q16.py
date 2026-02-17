# Write a program that takes as input the coefficients of the quadratic equation
# ax2 + bx + c = 0
# and prints whether the roots are real or complex.

a = int(input("Enter the co-efficient of X^2: "))
b = int(input("Enter the co-efficient of X: "))
c = int(input("Enter the Constant: "))

D = b ** 2 - 4 * a * c
if D >= 0:
    print("Real roots")
else:
    print("Complex roots")