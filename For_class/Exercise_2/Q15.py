'''15. Write a program that takes a point P(px, py) and determines the quadrant it lies in. Explicitly
handle the cases when the point lies on the axes or at the origin.'''

px, py = map(float, input("Enter the points: ").split())

if px == 0 and py == 0:
    print("The point lies on the origin")
elif px == 0 and py != 0:
    print("The point lies on the Y-axis")
elif px != 0 and py == 0:
    print("The point lies on the X-axis")
elif px > 0 and py > 0:
    print("The point lies in Quadrant 1")
elif px < 0 and py < 0:
    print("The point lies in Quadrant 3")
elif px > 0 and py < 0:
    print("The point lies in Quadrant 4")
else:
    print("The point lies in Quadrant 2")