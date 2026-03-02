secret = int(input("Enter secret number (keep it hidden): "))
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        print("Total attempts:", attempts)
        break