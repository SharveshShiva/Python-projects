import random
import art

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the total score from a list of cards."""
    score = sum(cards)

    # Check for blackjack (2 cards: Ace + 10)
    if score == 21 and len(cards) == 2:
        return 0  # 0 represents a Blackjack

    # Adjust Ace (11 → 1) if total score > 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares user score and computer score and returns result message."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😁"
    else:
        return "You lose 😤"


def play_game():
    """Main function that runs one game of Blackjack."""
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal initial 2 cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game-ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards while under 17 and not blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

