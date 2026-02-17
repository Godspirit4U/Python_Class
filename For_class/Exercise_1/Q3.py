# Write a simple calculator program. It should be able to add, subtract, multiply, and divide
# any two numbers input by the user.
# Note: The user will also specify the operation to perform.

print("MENU")
print("1) Add\n2) Subtract\n3) Multiply\n4) Divide")
option = int(input("Enter your choice: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match(option):
    case 1:
        print("Sum = ", num1 + num2)

    case 2:
        print("Difference", num1 - num2)

    case 3:
        print("Product", num1 * num2)

    case 4:
        try:
            print("Quotient = ", num1/num2)
        except:
            print("Division by zero is undefined!")

    case _:
        print("Invalid option!")
