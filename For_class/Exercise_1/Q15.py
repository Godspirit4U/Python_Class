# Write a program to select one option from the list and display output accordingly.
# Example:
# Please enter your choice:
# 1. Check Balance
# 2. View Offers
# 3. Special Recharge
# Enter 0 to exit
# (Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.)

while True:
    print("MENU")
    print("1) Check balance\n2) View offers\n3) Spevial recharge\n Enter 0 to exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        balance =  float(input("Enter initial amount"))
        print(balance)
    elif option == 2:
        print("**OFFERS**(viewed successfully)")
    elif option == 3:
        print("You have just received *Special Recharge*")
    elif option == 0:
        break
    else:
        print("Invalid option")
