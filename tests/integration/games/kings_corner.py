import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']

def card_value(card):
    rank = card[:-1]
    if rank == 'A':
        return 1
    if rank == 'J':
        return 11
    if rank == 'Q':
        return 12
    if rank == 'K':
        return 13
    return int(rank)

def opposite_color(card1, card2):
    red = ['♥', '♦']
    black = ['♠', '♣']
    return (card1[-1] in red and card2[-1] in black) or (card1[-1] in black and card2[-1] in red)

class Deck:
    def __init__(self):
        self.cards = [rank + suit for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self, n):
        return [self.cards.pop() for _ in range(n)]

class KingsInTheCorner:
    def __init__(self, num_players=2):
        self.deck = Deck()
        self.players = [self.deck.deal(7) for _ in range(num_players)]
        self.piles = [self.deck.deal(1)[0] for _ in range(4)]  # N, E, S, W
        self.corners = [None] * 4  # NE, SE, SW, NW
        self.turn = 0

    def show_board(self):
        print("\nBoard:")
        print(f" N:{self.piles[0]}  NE:{self.corners[0]}")
        print(f"W:{self.piles[3]}      E:{self.piles[1]}")
        print(f" S:{self.piles[2]}  SE:{self.corners[1]}")
        print(f"NW:{self.corners[3]}      SW:{self.corners[2]}")
        for i, hand in enumerate(self.players):
            print(f"Player {i+1} hand: {', '.join(hand)}")

    def play(self):
        while True:
            self.show_board()
            player = self.turn % len(self.players)
            hand = self.players[player]
            print(f"\nPlayer {player+1}'s turn.")
            move = input("Enter card to play (or 'draw' to draw): ").strip()
            if move == 'draw':
                if self.deck.cards:
                    card = self.deck.deal(1)[0]
                    hand.append(card)
                    print(f"Drew {card}")
                else:
                    print("Deck is empty.")
            elif move in hand:
                pile = input("Play to pile (N/E/S/W/NE/SE/SW/NW): ").strip().upper()
                idx = {'N':0, 'E':1, 'S':2, 'W':3, 'NE':0, 'SE':1, 'SW':2, 'NW':3}
                if pile in ['N','E','S','W']:
                    top = self.piles[idx[pile]]
                    if opposite_color(move, top) and card_value(move) == card_value(top) - 1:
                        self.piles[idx[pile]] = move
                        hand.remove(move)
                        print(f"Played {move} to {pile}")
                    else:
                        print("Invalid move.")
                elif pile in ['NE','SE','SW','NW']:
                    if move[-1] == 'K' and self.corners[idx[pile]] is None:
                        self.corners[idx[pile]] = move
                        hand.remove(move)
                        print(f"Placed King {move} in {pile} corner.")
                    else:
                        print("Invalid move.")
                else:
                    print("Unknown pile.")
            else:
                print("Card not in hand.")
            if not hand:
                print(f"Player {player+1} wins!")
                break
            self.turn += 1

if __name__ == "__main__":
    num_players = int(input("Number of players (2-4): "))
    game = KingsInTheCorner(num_players)
    game.play()