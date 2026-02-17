'''Write a program that takes three points (x1, y1), (x2, y2), and (x3, y3) and checks if they lie
on a straight line.'''

x1, y1 = map(float, input("Enter x1, y1: ").split())
x2, y2 = map(float, input("Enter x2, y2: ").split())
x3, y3 = map(float, input("Enter x3, y3: ").split())
is_in_line = 0
if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
    is_in_line = 1
print("The given points are in a straight line" if is_in_line == 1 else "The given points are not in a straight line")