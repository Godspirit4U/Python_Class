age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ").lower()
health = input("Enter health condition (excellent/poor): ").lower()
location = input("Enter location (city/village): ").lower()
policy_requested = int(input("Enter policy amount required: "))

if age < 25 or age > 65:
    print("Person is not eligible for insurance.")
else:
    if health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "male":
        max_policy = 200000
        base_premium = 4000

    elif health == "excellent" and 25 <= age <= 35 and location == "city" and gender == "female":
        max_policy = 150000
        base_premium = 3000

    elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
        max_policy = 100000
        base_premium = 6000

    else:
        max_policy = 125000
        base_premium = 5000

    if policy_requested > max_policy:
        print("Requested policy exceeds maximum allowed.")
        print("Maximum policy allowed:", max_policy)
    else:

        premium = (policy_requested / max_policy) * base_premium
        print("Policy approved!")
        print("Maximum policy allowed:", max_policy)
        print("Monthly premium to be paid: Rs.", premium)
