days = int(input("Enter number of days late: "))

if days <= 5:
    fine = days * 0.50
    print("Fine : Rs.", fine)

elif days <= 10:
    fine = days * 1
    print("Fine : Rs.", fine)

elif days <= 30:
    fine = days * 5
    print("Fine : Rs.", fine)

else:
    print("Membership cancelled due to late return.")
