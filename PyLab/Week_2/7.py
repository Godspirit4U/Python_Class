balance = 0

while True:
    print("\n===== ATM MENU =====\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit\n====================\n")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        balance += amount
        print("New balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("New balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you!")
        break
