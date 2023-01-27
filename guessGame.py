import random
for x in range(1, 7):
    guessNumber = int(input("Enter your guess number (1-6):"))

    randomNumber = random.randint(1, 6)

    if guessNumber == randomNumber:
        print("You have won.")
    else:
        print(f"You lost. Because random number was {randomNumber}")
