print("\n-----------------------------------------")
print("----- Insurence Premium Calculation -----")
print("-----------------------------------------")

health_status = print("What is your health status?\n\t1) Excellent\n\t2) Poor")
if health_status != 1 or health_status != 2:
    print("Ivvalid option!")
    exit()
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid Input.")
lives_in = print("Where do you live?\n\t1) City\n\t2) Village")
if lives_in != 1 or lives_in != 2:
    print("Ivvalid option!")
    exit()
gender = print("What is your gender?\n\t1) Male\n\t2) Female")
if gender != 1 or gender != 2:
    print("Ivvalid option!")
    exit()
try:
    policy_value = int(input("Enter your required policy value: "))
except ValueError:
    print("Invalid Input.")

if health_status == 1 and age >= 25 and age < 35 and lives_in == 1 and gender == 1:
    if policy_value > 200000:
        print("Policy amount cannot exceed ₹200000")
        exit()
    else:
        print("Premium is Rs. 4000 per month.")
elif health_status == 1 and age >= 25 and age < 35 and lives_in == 1 and gender == 2:
    if policy_value > 150000:
        print("Policy amount cannot exceed ₹150000")
        exit()
    else:
        print("Premium is Rs. 3000 per month.")
elif health_status == 2 and age >= 25 and age < 35 and lives_in == 2 and gender == 1:
    if policy_value > 100000:
        print("Policy amount cannot exceed ₹100000")
        exit()
    else:
        print("Premium is Rs. 6000 per month.")
elif age < 25 or age > 65:
    print("Poliy do not apply for you.")
else:
    if policy_value > 125000:
        print("Policy amount cannot exceed ₹125000")
        exit()
    else:
        print("Premium is Rs. 5000 per month.")

if policy_value < 123456:
    