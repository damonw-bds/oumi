import random
from typing import List, Tuple

# Define suits and ranks
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Create a deck of cards
def create_deck() -> List[Tuple[str, str]]:
    return [(rank, suit) for suit in SUITS for rank in RANKS]

# Deal cards to players
def deal_cards(deck: List[Tuple[str, str]]) -> List[List[Tuple[str, str]]]:
    random.shuffle(deck)
    return [deck[i::4] for i in range(4)]

# Get player bids
def get_bids() -> List[int]:
    bids = []
    for i in range(4):
        bid = int(input(f"Player {i + 1}, enter your bid (0-13): "))
        bids.append(bid)
    return bids

# Play a single trick
def play_trick(hands: List[List[Tuple[str, str]]], lead_suit: str = None) -> Tuple[int, str]:
    trick = []
    for i in range(4):
        print(f"Player {i + 1}'s hand: {hands[i]}")
        card = hands[i].pop(int(input(f"Player {i + 1}, choose a card to play (0-{len(hands[i]) - 1}): ")))
        trick.append(card)
        if lead_suit is None:
            lead_suit = card[1]
    print(f"Trick: {trick}")
    winning_card = max((card for card in trick if card[1] == lead_suit or card[1] == "Spades"),
                       key=lambda c: (SUITS.index(c[1]), RANKS.index(c[0])))
    winner = trick.index(winning_card)
    print(f"Player {winner + 1} wins the trick with {winning_card}")
    return winner, lead_suit

# Main game loop
def play_spades():
    deck = create_deck()
    hands = deal_cards(deck)
    bids = get_bids()
    scores = [0] * 4
    tricks_won = [0] * 4

    for _ in range(13):  # 13 tricks in a game
        lead_suit = None
        winner, lead_suit = play_trick(hands, lead_suit)
        tricks_won[winner] += 1

    # Calculate scores
    for i in range(4):
        if tricks_won[i] >= bids[i]:
            scores[i] += 10 * bids[i]
        else:
            scores[i] -= 10 * bids[i]
        scores[i] += tricks_won[i] - bids[i]  # Add 1 point for each overtrick

    print("Final Scores:")
    for i in range(4):
        print(f"Player {i + 1}: {scores[i]}")

if __name__ == "__main__":
    play_spades()