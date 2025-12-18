import random

def is_valid_guess(guess: str) -> bool:
    return guess.isdigit() and 1 <= int(guess) <= 100


def get_user_guess(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if is_valid_guess(user_input):
            return int(user_input)
        print("Invalid input. Please enter a number between 1 and 100.")


def play_guessing_game():
    target_number = random.randint(1, 100)
    guess_count = 0

    while True:
        guess = get_user_guess("Guess a number between 1 and 100: ")
        guess_count += 1

        if guess < target_number:
            print("Too low. Guess again.")
        elif guess > target_number:
            print("Too high. Guess again.")
        else:
            print(f"You guessed it in {guess_count} guesses!")
            break

play_guessing_game()
