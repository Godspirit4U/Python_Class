'''Write a program that takes as input n1 o1 n2 : o2 n3, where n1, n2, n3 are natural numbers
and o1, o2 ∈ {+,−, ∗}. Use nested if--else--if statements to evaluate the expression.'''

n1 = float(input("Enter n1: "))
o1 = input("Enter o1: ")
n2 = float(input("Enter n2: "))
o2 = input("Enter o2: ")
n3 = float(input("Enter n3: "))
if o1 == '+':
    if o2 == '-':
        value = n1 + n2 - n3
    elif o2 == '*':
        value = n2 + n2 * n3
    elif o2 == '+':
        value = n1 + n2 + n3
elif o1 == '-':
    if o2 == '+':
        value = n1 - n2 + n3
    elif o2 == '*':
        value = n2 - n2 * n3
    elif o2 == '-':
        value = n1 - n2 - n3
elif o1 == '*':
    if o2 == '+':
        value = n1 * n2 + n3
    elif o2 == '-':
        value = n2 * n2 - n3
    elif o2 == '*':
        value = n1 * n2 * n3
else:
    print("Invalid input")
print(value)