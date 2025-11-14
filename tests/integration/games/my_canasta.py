import random
from collections import Counter

# Define the ranks and suits of a standard deck of cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
WILDCARDS = ['2', 'Joker']  # 2s and Jokers are wild in Canasta

# Create a deck of cards (two standard decks for Canasta)
def create_deck():
    deck = []
    for _ in range(2):  # Two decks
        for suit in SUITS:
            for rank in RANKS:
                deck.append(f"{rank} of {suit}")
        deck.extend(["Joker"] * 2)  # Add Jokers
    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards to players
def deal_cards(deck, num_players=2):
    hands = {f"Player {i+1}": [] for i in range(num_players)}
    for _ in range(11):  # Each player gets 11 cards
        for player in hands:
            hands[player].append(deck.pop())
    return hands

# Draw a card from the deck
def draw_card(deck, hand):
    if deck:
        hand.append(deck.pop())
    else:
        print("The deck is empty!")

# Check if a meld is valid
def is_valid_meld(cards):
    if len(cards) < 3:
        return False
    ranks = [card.split()[0] for card in cards if card != "Joker"]
    wildcards = [card for card in cards if card in WILDCARDS or card == "Joker"]
    if len(set(ranks)) == 1 or (len(set(ranks)) == 0 and len(wildcards) > 0):
        return True
    return False

# Calculate the score of a meld
def calculate_meld_score(meld):
    score = 0
    for card in meld:
        rank = card.split()[0]
        if rank in WILDCARDS or card == "Joker":
            score += 20
        elif rank in ['8', '9', '10', 'J', 'Q', 'K']:
            score += 10
        elif rank in ['4', '5', '6', '7']:
            score += 5
        elif rank == 'A':
            score += 20
    return score

# Main game loop
def play_canasta():
    deck = create_deck()
    shuffle_deck(deck)
    hands = deal_cards(deck)
    melds = {player: [] for player in hands}
    discard_pile = []

    print("Welcome to Canasta!")
    print("Dealing cards...")
    for player, hand in hands.items():
        print(f"{player}'s hand: {hand}")

    turn = 0
    while deck:
        current_player = f"Player {turn % len(hands) + 1}"
        print(f"\n{current_player}'s turn:")
        print(f"Your hand: {hands[current_player]}")

        # Draw a card
        print("Drawing a card...")
        draw_card(deck, hands[current_player])
        print(f"Your hand after drawing: {hands[current_player]}")

        # Attempt to meld
        print("Attempting to meld...")
        meld = input("Enter the cards you want to meld (comma-separated): ").split(", ")
        if all(card in hands[current_player] for card in meld):
            if is_valid_meld(meld):
                melds[current_player].append(meld)
                for card in meld:
                    hands[current_player].remove(card)
                print(f"Valid meld! Melded: {meld}")
            else:
                print("Invalid meld!")
        else:
            print("You don't have those cards!")

        # Discard a card
        discard = input("Enter a card to discard: ")
        if discard in hands[current_player]:
            hands[current_player].remove(discard)
            discard_pile.append(discard)
            print(f"Discarded: {discard}")
        else:
            print("You don't have that card!")

        # Check if the player has emptied their hand
        if not hands[current_player]:
            print(f"{current_player} has emptied their hand! The round ends.")
            break

        turn += 1

    # Calculate scores
    print("\nGame over! Calculating scores...")
    for player, player_melds in melds.items():
        score = sum(calculate_meld_score(meld) for meld in player_melds)
        print(f"{player}'s score: {score}")

if __name__ == "__main__":
    play_canasta()