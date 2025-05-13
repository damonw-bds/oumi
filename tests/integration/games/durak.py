import random

# Define the suits and ranks of a standard deck of cards
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        return RANKS.index(self.rank) < RANKS.index(other.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, count):
        for _ in range(count):
            card = deck.draw()
            if card:
                self.hand.append(card)

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

    def play_card(self, card):
        self.hand.remove(card)
        return card

class DurakGame:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.trump = self.deck.cards[-1].suit  # Last card determines the trump suit
        self.players = [Player(player1_name), Player(player2_name)]
        self.attacker = self.players[0]
        self.defender = self.players[1]

        # Deal 6 cards to each player
        for player in self.players:
            player.draw_cards(self.deck, 6)

    def is_trump(self, card):
        return card.suit == self.trump

    def can_defend(self, attack_card, defense_card):
        if self.is_trump(defense_card) and not self.is_trump(attack_card):
            return True
        if attack_card.suit == defense_card.suit and defense_card > attack_card:
            return True
        return False

    def play_turn(self):
        print(f"\nTrump suit: {self.trump}")
        print(f"{self.attacker.name}'s hand: {self.attacker.show_hand()}")
        print(f"{self.defender.name}'s hand: {self.defender.show_hand()}")

        # Attacker plays a card
        attack_card = self.attacker.hand[0]
        print(f"{self.attacker.name} attacks with {attack_card}")
        self.attacker.play_card(attack_card)

        # Defender tries to defend
        defense_card = None
        for card in self.defender.hand:
            if self.can_defend(attack_card, card):
                defense_card = card
                break

        if defense_card:
            print(f"{self.defender.name} defends with {defense_card}")
            self.defender.play_card(defense_card)
        else:
            print(f"{self.defender.name} cannot defend and takes the card!")
            self.defender.hand.append(attack_card)

        # Refill hands to 6 cards
        for player in self.players:
            player.draw_cards(self.deck, 6 - len(player.hand))

        # Swap roles
        self.attacker, self.defender = self.defender, self.attacker

    def is_game_over(self):
        return any(len(player.hand) == 0 for player in self.players) or not self.deck.cards

    def play_game(self):
        print("Starting Durak!")
        while not self.is_game_over():
            self.play_turn()

        if len(self.attacker.hand) == 0:
            print(f"{self.attacker.name} wins! {self.defender.name} is the Durak!")
        elif len(self.defender.hand) == 0:
            print(f"{self.defender.name} wins! {self.attacker.name} is the Durak!")
        else:
            print("Game over! No cards left in the deck.")

# Example usage
if __name__ == "__main__":
    game = DurakGame("Player 1", "Player 2")
    game.play_game()