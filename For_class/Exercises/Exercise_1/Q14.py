# Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
# respective grade point (10/9/8/7/6/4).
# Note: If an invalid letter grade is entered, the program should display an appropriate
# message.

grades = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 4
}

grade = input("Enter the grade(S,A,B,C,D,E): ")
try:
    print(grades[grade])
except:
    print("Invalid Input!")
