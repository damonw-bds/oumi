# Canasta game implementation (simplified)

import random
from collections import defaultdict

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
WILD_CARDS = ['2', 'Joker']

def create_deck():
    deck = []
    for _ in range(2):  # Two decks
        for suit in SUITS:
            for rank in RANKS:
                deck.append((rank, suit))
        deck += [('Joker', None)] * 2
    random.shuffle(deck)
    return deck

def deal_hands(deck, num_players=2):
    hands = [[] for _ in range(num_players)]
    for _ in range(11):
        for hand in hands:
            hand.append(deck.pop())
    return hands

def draw_card(deck, discard_pile):
    if deck:
        return deck.pop()
    else:
        # If deck is empty, shuffle discard pile (except top card)
        top = discard_pile.pop()
        deck[:] = discard_pile
        random.shuffle(deck)
        discard_pile[:] = [top]
        return deck.pop()

def can_meld(cards):
    ranks = [card[0] for card in cards]
    if len(set(ranks)) == 1 and len(cards) >= 3:
        return True
    return False

def score_meld(meld):
    rank = meld[0][0]
    if rank == 'A':
        return 20 * len(meld)
    elif rank in ['2', 'Joker']:
        return 20 * len(meld)
    elif rank in ['8', '9', '10', 'J', 'Q', 'K']:
        return 10 * len(meld)
    else:
        return 5 * len(meld)

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.melds = []

    def show_hand(self):
        return ', '.join([f"{r} of {s}" if s else r for r, s in self.hand])

    def meld(self, cards):
        for card in cards:
            self.hand.remove(card)
        self.melds.append(cards)

    def draw(self, deck, discard_pile):
        card = draw_card(deck, discard_pile)
        self.hand.append(card)
        print(f"{self.name} drew {card[0]} of {card[1] if card[1] else ''}")

    def discard(self, discard_pile):
        card = random.choice(self.hand)
        self.hand.remove(card)
        discard_pile.append(card)
        print(f"{self.name} discarded {card[0]} of {card[1] if card[1] else ''}")

def play_canasta():
    deck = create_deck()
    hands = deal_hands(deck)
    players = [Player(f"Player {i+1}", hands[i]) for i in range(2)]
    discard_pile = [deck.pop()]

    turn = 0
    while all(len(p.hand) > 0 for p in players):
        player = players[turn % 2]
        print(f"\n{player.name}'s turn. Hand: {player.show_hand()}")
        player.draw(deck, discard_pile)

        # Try to meld
        meld_candidates = defaultdict(list)
        for card in player.hand:
            meld_candidates[card[0]].append(card)
        for rank, cards in meld_candidates.items():
            if can_meld(cards):
                print(f"{player.name} melds {len(cards)} {rank}s")
                player.meld(cards)
                break

        player.discard(discard_pile)
        turn += 1

    # Scoring
    for player in players:
        meld_score = sum(score_meld(meld) for meld in player.melds)
        print(f"{player.name} melds: {player.melds}, score: {meld_score}")

if __name__ == "__main__":
    play_canasta()