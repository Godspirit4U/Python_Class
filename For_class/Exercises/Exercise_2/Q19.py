time = float(input("Enter time taken to complete the job (in hours): "))

if time <= 2:
    print("Highly efficient worker")

elif time <= 3:
    print("Worker should improve speed")

elif time <= 4:
    print("Worker needs training")

else:
    print("Worker has to leave the company")
