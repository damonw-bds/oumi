import random
from itertools import combinations

# Define the ranks and suits of a standard deck of cards
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a deck of cards
def create_deck():
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards to players
def deal_hole_cards(deck, num_players):
    return [[deck.pop() for _ in range(2)] for _ in range(num_players)]

# Deal community cards
def deal_community_cards(deck):
    return [deck.pop() for _ in range(5)]

# Evaluate hand rankings (simplified version)
def evaluate_hand(hand):
    # This is a placeholder for hand evaluation logic
    # In a real implementation, you would calculate the best 5-card hand
    # and rank it based on poker rules
    return random.randint(1, 100)  # Random score for simplicity

# Determine the winner
def determine_winner(players_hands, community_cards):
    scores = []
    for i, hand in enumerate(players_hands):
        combined_hand = hand + community_cards
        best_hand_score = max(evaluate_hand(list(combo)) for combo in combinations(combined_hand, 5))
        scores.append((i, best_hand_score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]  # Return the index of the winning player

# Main game logic
def texas_holdem(num_players):
    if num_players < 2 or num_players > 10:
        print("Texas Hold'em requires 2-10 players.")
        return

    # Initialize the deck and shuffle it
    deck = create_deck()
    shuffle_deck(deck)

    # Deal hole cards to players
    players_hands = deal_hole_cards(deck, num_players)
    print("\nPlayer Hands:")
    for i, hand in enumerate(players_hands):
        print(f"Player {i + 1}: {hand}")

    # Deal community cards
    community_cards = deal_community_cards(deck)
    print("\nCommunity Cards:")
    print(community_cards)

    # Determine the winner
    winner = determine_winner(players_hands, community_cards)
    print(f"\nThe winner is Player {winner + 1}!")

# Run the game
if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2-10): "))
    texas_holdem(num_players)