import random

def number_guessing_game():
    """Plays a number guessing game with the user."""

    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    guess_count = 0

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            user_guess = int(input("Take a guess: "))
            guess_count += 1

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Your guess is outside the valid range of {lower_bound} to {upper_bound}. Please try again.")
            elif user_guess < secret_number:
                print("Too low! Try guessing higher.")
            elif user_guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {guess_count} guesses.")
                break  # Exit the loop when the guess is correct

        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()