import random

def my_func(level, random_me):
    """Handles the guessing logic."""
    while level > 0:
        print(f"\nYou have {level} attempts remaining to guess the number.")
        
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if user_guess > random_me:
            print("Too high!")
        elif user_guess < random_me:
            print("Too low!")
        else:
            print("🎉 You guessed it right!! 🎉")
            return

        level -= 1

    print(f"\nSorry, you lost! The correct number was {random_me}.")

def difficult():
    """Returns difficulty level (easy: 10 attempts, hard: 5 attempts)."""
    while True:
        diff_level = input("\nType 'easy' or 'hard' for difficulty level: ").lower()
        if diff_level == 'easy':
            return 10
        elif diff_level == 'hard':
            return 5
        else:
            print("Invalid choice! Please type 'easy' or 'hard'.")

while True:
    print("\nWelcome to the Number Guessing Game! 🎯")
    random_me = random.randint(1, 100)  # Generate a random number
    level = difficult()  # Get difficulty level
    my_func(level, random_me)  # Start the game

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye! 👋")
        break
