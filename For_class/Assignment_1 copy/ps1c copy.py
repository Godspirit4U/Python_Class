# take user input
while True:
    try:
        annual_salary = int(input("Enter starting salary: "))
        if annual_salary <= 0:
            print("Starting salary must greater than zero.")
            exit()
        break
    except ValueError:
        print("Invalid input! try again.")

# Given data and initial values
house_cost = 1000000
down_payment = house_cost * 0.25
annual_return = 0.04
semi_annual_raise = 0.07
savings = 0
# Monthly calculations
monthly_salary = annual_salary / 12
original_monthly_salary = monthly_salary
monthly_return = annual_return / 12

# loop for 36 months with 100% savings
for months in range(1, 37):
    savings += savings * monthly_return
    savings += monthly_salary * 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
if savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
    exit()
else:
    savings = 0

# initialising required variables
low_rate = 0
high_rate = 1
steps = 0

# looping until we find required savings rate

while True:
    mid_rate = (low_rate + high_rate) / 2
    savings = 0
    monthly_salary = original_monthly_salary
    for months in range(1, 37):
        savings += savings * monthly_return
        savings += monthly_salary * mid_rate
        if months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    steps += 1

    if abs(savings - down_payment) <= 100:
        print(f'Best savings rate: {mid_rate:.4f}')
        print(f'Steps in bisection search: {steps}')
        exit()

    elif savings < down_payment:
        low_rate = mid_rate
    else:
        high_rate = mid_rate
