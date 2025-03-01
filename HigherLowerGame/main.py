import random
from art import data
from day14.art import shape


def select(feed):
    """Function to randomly select a figure"""
    pick = random.randint(0, len(feed) - 1)
    random_select = feed[pick]
    return random_select


def update(my_two, element):
    """Function that updates the list in a way that player B will become A"""
    my_two[0] = my_two[1]
    my_two[1] = element
    return my_two


def compare(optionA, optionB, user):
    """Compare the followers number and the user answer"""
    if optionA > optionB:
        if user == "a":
            return +1
        else:
            return 0
    else:
        if user == "b":
            return +1
        else:
            return 0


def my_game():
    compare_list = [select(data), select(data)]  # Initialize two random selections
    score = 0  # Player's score
    level = 0  # Current level

    keep_playing = True  # Flag to keep playing

    while keep_playing:
        # Update the selection with a new random choice
        update(compare_list, select(data))

        # Display the figures and their details
        print(f"Compare A: {compare_list[0]['name']}, {compare_list[0]['description']} from {compare_list[0]['country']}")
        print(shape)
        print(f"Compare B: {compare_list[1]['name']}, {compare_list[1]['description']} from {compare_list[1]['country']}")

        # User's choice for which figure has more followers
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)  # Clean up the terminal screen

        # Compare the two figures' follower counts
        score += compare(compare_list[0]['follower_count'], compare_list[1]['follower_count'], user_choice)

        if score <= level:
            print(f"That's not right, your score: {score}")
            keep_playing = False  # End the game if the player makes a wrong choice
        else:
            level = score  # Update the level to the new score
            print(f"You're right! Current score: {score}")

# Start the game
if __name__ == "__main__":
    my_game()
