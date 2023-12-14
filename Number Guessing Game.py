import random

def number_guessing_game():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between {lower_limit} and {upper_limit}.")

    while attempts < max_attempts:
        user_guess = int(input("Enter your guess: "))

        if user_guess < lower_limit or user_guess > upper_limit:
            print(f"Please enter a number between {lower_limit} and {upper_limit}.")
            continue

        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

number_guessing_game()
