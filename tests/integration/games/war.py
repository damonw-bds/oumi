import random

class Card:
    """Represents a single playing card."""
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()

    def value(self):
        """Returns the value of the card for comparison."""
        return Card.RANKS.index(self.rank)

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck."""
        return self.cards.pop() if self.cards else None

class WarGame:
    """Represents the card game War."""
    def __init__(self):
        self.deck = Deck()
        self.player1_hand = []
        self.player2_hand = []

        # Split the deck between two players
        while self.deck.cards:
            self.player1_hand.append(self.deck.draw())
            self.player2_hand.append(self.deck.draw())

    def play_round(self):
        """Plays a single round of War."""
        if not self.player1_hand or not self.player2_hand:
            return

        card1 = self.player1_hand.pop(0)
        card2 = self.player2_hand.pop(0)

        print(f"Player 1 plays: {card1}")
        print(f"Player 2 plays: {card2}")

        if card1.value() > card2.value():
            print("Player 1 wins the round!")
            self.player1_hand.extend([card1, card2])
        elif card1.value() < card2.value():
            print("Player 2 wins the round!")
            self.player2_hand.extend([card1, card2])
        else:
            print("War!")
            self.handle_war([card1], [card2])

    def handle_war(self, war_pile1, war_pile2):
        """Handles a 'War' scenario."""
        if len(self.player1_hand) < 4 or len(self.player2_hand) < 4:
            print("A player does not have enough cards for war. Game over!")
            return

        # Add three face-down cards to the war pile
        for _ in range(3):
            if self.player1_hand:
                war_pile1.append(self.player1_hand.pop(0))
            if self.player2_hand:
                war_pile2.append(self.player2_hand.pop(0))

        # Play one face-up card
        if self.player1_hand:
            war_pile1.append(self.player1_hand.pop(0))
        if self.player2_hand:
            war_pile2.append(self.player2_hand.pop(0))

        print(f"Player 1's war pile: {war_pile1[-1]}")
        print(f"Player 2's war pile: {war_pile2[-1]}")

        if war_pile1[-1].value() > war_pile2[-1].value():
            print("Player 1 wins the war!")
            self.player1_hand.extend(war_pile1 + war_pile2)
        elif war_pile1[-1].value() < war_pile2[-1].value():
            print("Player 2 wins the war!")
            self.player2_hand.extend(war_pile1 + war_pile2)
        else:
            print("War continues!")
            self.handle_war(war_pile1, war_pile2)

    def check_winner(self):
        """Checks if there is a winner."""
        if not self.player1_hand:
            print("Player 2 wins the game!")
            return True
        elif not self.player2_hand:
            print("Player 1 wins the game!")
            return True
        return False

    def play_game(self):
        """Plays the game until there is a winner."""
        round_number = 1
        while not self.check_winner():
            print(f"\n--- Round {round_number} ---")
            self.play_round()
            round_number += 1

# Start a game of War
if __name__ == "__main__":
    game = WarGame()
    game.play_game()