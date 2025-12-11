"""
Number Guessing Game

This game generates a random number between 1 and 100 and allows the
player up to 7 attempts to guess it. The program demonstrates:
- for loops with fixed iterations
- break and continue statements
- input handling
- feedback and game logic
"""

import random


def number_guessing_game():
    """Main logic for the number guessing game."""
    target = random.randint(1, 100)
    attempts_used = 0
    player_won = False  # Track whether player guessed correctly

    print("\n--- Number Guessing Game ---")
    print("Guess the number between 1 and 100.")
    print("Type 'quit' anytime to exit.\n")

    for attempt in range(1, 8):  # 7 attempts
        guess = input(f"Attempt {attempt}/7 - Enter your guess: ")
        attempts_used = attempt

        # Quit game early
        if guess.lower() == "quit":
            print("\nYou chose to quit the game.")
            break

        # Validate numeric input
        try:
            guess_num = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue  # Skip the rest of this iteration

        # Compare guess with the target
        if guess_num == target:
            print("\n🎉 Correct! You guessed the number!")
            player_won = True
            break
        elif guess_num > target:
            print("Too high! Try again.\n")
            continue
        else:
            print("Too low! Try again.\n")
            continue

    # Game summary
    print("\n--- Game Summary ---")

    if player_won:
        print(f"You won in {attempts_used} attempts! Great job! 🎉")
    else:
        print("You lost! Better luck next time.")
        print(f"The correct number was: {target}")

    print("\nThanks for playing!\n")


# Run the game
if __name__ == "__main__":
    number_guessing_game()
