
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates and returns the score of the hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack!

    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1  # Convert Ace from 11 to 1 if over 21
    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer scores and returns the result."""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lost, the dealer has a Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lost!"
    elif computer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lost!"

def play_blackjack():
    """Main function to play a round of blackjack."""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to hit, or 'n' to stand: ").lower()
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)  # Clear screen effect
    play_blackjack()
