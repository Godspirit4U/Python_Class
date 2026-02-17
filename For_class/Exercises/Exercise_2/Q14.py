'''14. Write a program that takes as input:
• center of a circle (cx, cy),
• radius r,
• a point P(px, py),
and determines whether the point lies inside the circle, on the circle, or outside the circle.'''

c1, c2 = map(float, input("Enter the coords of centre of the circle: "))
radius = float(input("Enter the radius of the circle: "))
x1, x2 = map(float, input("Enter the coords of the point: "))

distance = ((c1 - x1) ** 2) + ((c2-x2) ** 2)
if distance < radius ** 2:
    print("The point lies inside the circle")
elif distance == radius ** 2:
    print("Point is on the circle")
else:
    print("The point lies outside the circle")