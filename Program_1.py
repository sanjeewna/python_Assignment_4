import random

def guess_the_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Start the game loop
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 10: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Correct! You guessed the right number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

#Start the game
guess_the_number()
