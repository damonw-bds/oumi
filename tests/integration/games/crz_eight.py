import random

# Define card suits and ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a deck of cards
def create_deck():
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]

# Draw a card from the deck
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Check if a card is playable
def is_playable(card, top_card, current_suit):
    if '8' in card:
        return True
    return card.split(' ')[-1] == current_suit or card.split(' ')[0] == top_card.split(' ')[0]

# Main game logic
def crazy_eights():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [draw_card(deck) for _ in range(5)]
    computer_hand = [draw_card(deck) for _ in range(5)]
    top_card = draw_card(deck)
    current_suit = top_card.split(' ')[-1]

    print(f"Starting card: {top_card}")
    print(f"Your hand: {player_hand}")

    while True:
        # Player's turn
        playable_cards = [card for card in player_hand if is_playable(card, top_card, current_suit)]
        if playable_cards:
            print(f"Playable cards: {playable_cards}")
            chosen_card = input("Choose a card to play: ")
            if chosen_card in playable_cards:
                player_hand.remove(chosen_card)
                top_card = chosen_card
                if '8' in chosen_card:
                    current_suit = input("Choose a new suit (Hearts, Diamonds, Clubs, Spades): ")
                else:
                    current_suit = top_card.split(' ')[-1]
            else:
                print("Invalid choice. Try again.")
                continue
        else:
            print("No playable cards. Drawing a card...")
            player_hand.append(draw_card(deck))

        if not player_hand:
            print("You win!")
            break

        # Computer's turn
        computer_playable = [card for card in computer_hand if is_playable(card, top_card, current_suit)]
        if computer_playable:
            chosen_card = random.choice(computer_playable)
            computer_hand.remove(chosen_card)
            top_card = chosen_card
            if '8' in chosen_card:
                current_suit = random.choice(SUITS)
            else:
                current_suit = top_card.split(' ')[-1]
            print(f"Computer played: {chosen_card}")
        else:
            print("Computer has no playable cards. Drawing a card...")
            computer_hand.append(draw_card(deck))

        if not computer_hand:
            print("Computer wins!")
            break

        print(f"Top card: {top_card}")
        print(f"Your hand: {player_hand}")

# Run the game
if __name__ == "__main__":
    crazy_eights()