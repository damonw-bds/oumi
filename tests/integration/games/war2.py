import random

# Define the suits and ranks of a standard deck of cards
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def value(self):
        return RANKS.index(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        return self.hand.pop(0) if self.hand else None

    def add_cards(self, cards):
        self.hand.extend(cards)

    def has_cards(self):
        return len(self.hand) > 0

class WarGame:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name), Player(player2_name)]
        self.deck = Deck()
        self.deal_cards()

    def deal_cards(self):
        while self.deck.cards:
            self.players[0].add_cards([self.deck.deal()])
            self.players[1].add_cards([self.deck.deal()])

    def play_round(self):
        print(f"\n{self.players[0].name} has {len(self.players[0].hand)} cards.")
        print(f"{self.players[1].name} has {len(self.players[1].hand)} cards.")

        card1 = self.players[0].draw_card()
        card2 = self.players[1].draw_card()

        print(f"{self.players[0].name} plays {card1}")
        print(f"{self.players[1].name} plays {card2}")

        if card1.value() > card2.value():
            print(f"{self.players[0].name} wins the round!")
            self.players[0].add_cards([card1, card2])
        elif card1.value() < card2.value():
            print(f"{self.players[1].name} wins the round!")
            self.players[1].add_cards([card1, card2])
        else:
            print("War!")
            self.handle_war([card1, card2])

    def handle_war(self, war_pile):
        if len(self.players[0].hand) < 4 or len(self.players[1].hand) < 4:
            print("A player does not have enough cards for war. Game over!")
            return

        war_pile.extend([self.players[0].draw_card() for _ in range(3)])
        war_pile.extend([self.players[1].draw_card() for _ in range(3)])

        card1 = self.players[0].draw_card()
        card2 = self.players[1].draw_card()

        print(f"{self.players[0].name} plays {card1} in war.")
        print(f"{self.players[1].name} plays {card2} in war.")

        if card1.value() > card2.value():
            print(f"{self.players[0].name} wins the war!")
            self.players[0].add_cards(war_pile + [card1, card2])
        elif card1.value() < card2.value():
            print(f"{self.players[1].name} wins the war!")
            self.players[1].add_cards(war_pile + [card1, card2])
        else:
            print("War continues!")
            self.handle_war(war_pile + [card1, card2])

    def is_game_over(self):
        return not self.players[0].has_cards() or not self.players[1].has_cards()

    def play_game(self):
        print("Starting War!")
        while not self.is_game_over():
            self.play_round()

        if self.players[0].has_cards():
            print(f"{self.players[0].name} wins the game!")
        else:
            print(f"{self.players[1].name} wins the game!")

# Example usage
if __name__ == "__main__":
    game = WarGame("Player 1", "Player 2")
    game.play_game()