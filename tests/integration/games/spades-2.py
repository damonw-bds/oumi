import random
from collections import defaultdict

SUITS = ['S', 'H', 'D', 'C']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
PLAYERS = ['North', 'East', 'South', 'West']

def make_deck():
    return [r + s for s in SUITS for r in RANKS]

def card_value(card):
    rank, suit = card[:-1], card[-1]
    return (SUITS.index(suit), RANKS.index(rank))

def deal():
    deck = make_deck()
    random.shuffle(deck)
    return [deck[i*13:(i+1)*13] for i in range(4)]

def ai_bid(hand):
    # Simple AI: bid number of spades + high cards
    spades = [c for c in hand if c[-1] == 'S']
    high = [c for c in hand if c[:-1] in ['A', 'K', 'Q']]
    return max(1, len(spades) + len(high) // 4)

def valid_plays(hand, trick, spades_broken):
    if not trick:
        # Lead: can't lead spades unless broken or only spades left
        if spades_broken or all(c[-1] == 'S' for c in hand):
            return hand
        return [c for c in hand if c[-1] != 'S']
    lead_suit = trick[0][1][-1]
    follow = [c for c in hand if c[-1] == lead_suit]
    return follow if follow else hand

def winner(trick):
    lead_suit = trick[0][1][-1]
    spades = [(i, c) for i, c in trick if c[-1] == 'S']
    if spades:
        return max(spades, key=lambda x: RANKS.index(x[1][:-1]))[0]
    lead = [(i, c) for i, c in trick if c[-1] == lead_suit]
    return max(lead, key=lambda x: RANKS.index(x[1][:-1]))[0]

def play_game():
    hands = deal()
    for h in hands:
        h.sort(key=lambda c: (SUITS.index(c[-1]), RANKS.index(c[:-1])))
    bids = [ai_bid(h) for h in hands]
    print("Bids:", dict(zip(PLAYERS, bids)))
    tricks_won = [0, 0, 0, 0]
    spades_broken = False
    leader = 0
    for trick_num in range(13):
        trick = []
        for i in range(4):
            player = (leader + i) % 4
            hand = hands[player]
            options = valid_plays(hand, trick, spades_broken)
            card = random.choice(options)
            hand.remove(card)
            trick.append((player, card))
            if card[-1] == 'S' and not spades_broken:
                spades_broken = True
        win = winner(trick)
        tricks_won[win] += 1
        leader = win
        print(f"Trick {trick_num+1}: " + ", ".join(f"{PLAYERS[p]}:{c}" for p, c in trick) + f" | Winner: {PLAYERS[win]}")
    # Scoring
    scores = []
    for i in range(4):
        if tricks_won[i] >= bids[i]:
            score = 10 * bids[i] + (tricks_won[i] - bids[i])
        else:
            score = -10 * bids[i]
        scores.append(score)
    print("Tricks won:", dict(zip(PLAYERS, tricks_won)))
    print("Scores:", dict(zip(PLAYERS, scores)))

if __name__ == "__main__":
    play_game()