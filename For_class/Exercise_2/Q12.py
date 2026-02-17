'''Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter. Also print whether the area is greater than the perimeter.'''

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
perimeter = 2 * (length + breadth)
area = length * breadth
print(f'Area = {area}\nPerimeter = {perimeter}')
if area == perimeter:
    print('Area is equal to perimeter')
else:
    print('Area is greater then perimeter' if area > perimeter else 'perimeter is greater then area')