# Take user inputs
while True:
    try:
        annual_salary = int(input("Enter your annual salary: "))
        if annual_salary <= 0:
            print("Salary must be greater than 0.")
            exit()
        break
    except ValueError:
        print("Invalid input! try again.")
while True:
    try:
        portion_saved = float(
            input("Enter the percent of your salary to save, as a decimal: "))
        if portion_saved == 0:
            print("Savings rate must be greater than 0.")
            exit()
        elif portion_saved < 0:
            print("Savings rate cannot be negative.")
            exit()
        elif portion_saved > 1:
            print("Savings rate cannot exceed salary.")
            exit()
        break
    except ValueError:
        print("Invalid input! try again.")
while True:
    try:
        cost_of_dreamhome = int(input("Enter the cost of your dream home: "))
        if cost_of_dreamhome <= 0:
            print("Cost of dream home cannot be less than zero.")
            exit()
        break
    except ValueError:
        print("Invalid input! try again.")

# given data and initial values
down_payment = 0.25 * cost_of_dreamhome
savings = 0
annual_investment_return = 0.04

# monthly calculations
monthly_salary = annual_salary / 12
monthly_investment_return = annual_investment_return / 12
monthly_saving = portion_saved * monthly_salary

# counter for months
months = 0

# Loop until savings reach down payment
while savings < down_payment:
    # add investment return
    savings += savings * monthly_investment_return

    # add monthly savings from salary
    savings += monthly_saving

    # increment months count
    months += 1

# display result
print("Number of months:", months)
