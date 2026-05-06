import random
from collections import Counter

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def create_deck():
    return [r + s for r in RANKS for s in SUITS]

def deal(deck, n):
    return [deck.pop() for _ in range(n)]

def hand_rank(hand):
    # Simplified: only checks for pairs and high card
    ranks = sorted([RANKS.index(card[0]) for card in hand], reverse=True)
    counts = Counter([card[0] for card in hand])
    if 4 in counts.values():
        return (7, ranks)  # Four of a kind
    elif sorted(counts.values()) == [2, 3]:
        return (6, ranks)  # Full house
    elif 3 in counts.values():
        return (3, ranks)  # Three of a kind
    elif list(counts.values()).count(2) == 2:
        return (2, ranks)  # Two pair
    elif 2 in counts.values():
        return (1, ranks)  # One pair
    else:
        return (0, ranks)  # High card

def best_hand(seven_cards):
    from itertools import combinations
    return max([hand_rank(list(combo)) for combo in combinations(seven_cards, 5)])

def play_texas_holdem(num_players=2):
    deck = create_deck()
    random.shuffle(deck)
    players = [deal(deck, 2) for _ in range(num_players)]
    print("Players' hands:")
    for i, hand in enumerate(players):
        print(f"Player {i+1}: {hand}")
    print()
    # Deal community cards
    flop = deal(deck, 3)
    turn = deal(deck, 1)
    river = deal(deck, 1)
    community = flop + turn + river
    print(f"Community cards: {community}")
    print()
    # Showdown
    scores = []
    for i, hand in enumerate(players):
        score = best_hand(hand + community)
        scores.append((score, i))
        print(f"Player {i+1} best hand: {score}")
    winner = max(scores)[1]
    print(f"\nWinner: Player {winner+1}")

if __name__ == "__main__":
    play_texas_holdem(2)