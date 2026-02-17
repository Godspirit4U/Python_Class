# Write a program that takes the length and breadth of a rectangle as input and prints its area
# and perimeter.
# Note: If the inputs are invalid, display an appropriate message.
length = input("Enter the length of rectangle: ")
breadth = input("Enter the breadth of rectangle: ")

if length.isdigit() and breadth.isdigit() and int(length) >= 0 and int(breadth) >= 0:
    length = int(length)
    breadth = int(breadth)
    print("Perimeter = ", 2 * (length + breadth))
    print("Area = ", length * breadth)
else:
    print("Input Invalid!")
