# Write a program that takes the radius of a circle as input and computes its area.
# Note: If the radius is non-negative, display an appropriate message.

radius_of_circle = int(input("Enter the radius of circle : "))
if radius_of_circle < 0:
    print("Radius cannot be negative!")
else:
    area_of_circle = 3.14 * (radius_of_circle ** 2)
    print(f'Area of circle is {area_of_circle}')
