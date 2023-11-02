import random

def guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

guessing_game()
