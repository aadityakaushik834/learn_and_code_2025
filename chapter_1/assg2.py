import random

def is_valid_guess(user_input: str) -> bool:
    return user_input.isdigit() and 1 <= int(user_input) <= 100

def start_number_guessing_game():
    secret_number = random.randint(1, 100)
    has_guessed_correctly = False
    number_of_attempts = 0

    user_guess = input("Guess a number between 1 and 100: ")

    while not has_guessed_correctly:

        if not is_valid_guess(user_guess):
            user_guess = input("Invalid input. Please enter a number between 1 and 100: ")
            continue
        else:
            number_of_attempts += 1
            guessed_value = int(user_guess)

        if guessed_value < secret_number:
            user_guess = input("Too low. Try again: ")
        elif guessed_value > secret_number:
            user_guess = input("Too high. Try again: ")
        else:
            print(f"Correct! You guessed the number in {number_of_attempts} attempts.")
            has_guessed_correctly = True

start_number_guessing_game()