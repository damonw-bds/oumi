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

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self):
        """Draws a card from the deck."""
        if self.cards:
            return self.cards.pop()
        else:
            return None

class RummyGame:
    """Represents a simplified version of the Rummy card game."""
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = Deck()
        self.players_hands = [[] for _ in range(num_players)]
        self.discard_pile = []

        # Deal 7 cards to each player
        for _ in range(7):
            for hand in self.players_hands:
                hand.append(self.deck.draw())

    def draw_card(self, player_index):
        """Allows a player to draw a card from the deck or discard pile."""
        if not self.deck.cards:
            print("The deck is empty!")
            return None

        card = self.deck.draw()
        self.players_hands[player_index].append(card)
        return card

    def discard_card(self, player_index, card_index):
        """Allows a player to discard a card."""
        card = self.players_hands[player_index].pop(card_index)
        self.discard_pile.append(card)
        return card

    def check_meld(self, cards):
        """Checks if a set of cards forms a valid meld (set or run)."""
        if len(cards) < 3:
            return False

        # Check for a set (same rank, different suits)
        if all(card.rank == cards[0].rank for card in cards):
            return True

        # Check for a run (consecutive ranks, same suit)
        sorted_cards = sorted(cards, key=lambda c: Card.RANKS.index(c.rank))
        if all(
            Card.RANKS.index(sorted_cards[i + 1].rank) - Card.RANKS.index(sorted_cards[i].rank) == 1
            and sorted_cards[i].suit == sorted_cards[i + 1].suit
            for i in range(len(sorted_cards) - 1)
        ):
            return True

        return False

    def play_turn(self, player_index):
        """Simulates a player's turn."""
        print(f"Player {player_index + 1}'s turn:")
        print("Your hand:", self.players_hands[player_index])

        # Draw a card
        drawn_card = self.draw_card(player_index)
        print(f"You drew: {drawn_card}")

        # Discard a card
        print("Your hand after drawing:", self.players_hands[player_index])
        discard_index = int(input("Enter the index of the card to discard: "))
        discarded_card = self.discard_card(player_index, discard_index)
        print(f"You discarded: {discarded_card}")

    def check_winner(self):
        """Checks if any player has won the game."""
        for i, hand in enumerate(self.players_hands):
            if self.check_meld(hand):
                return i
        return None

    def play_game(self):
        """Runs the game loop."""
        while True:
            for player_index in range(self.num_players):
                self.play_turn(player_index)
                winner = self.check_winner()
                if winner is not None:
                    print(f"Player {winner + 1} wins!")
                    return

# Start a game of Rummy with 2 players
if __name__ == "__main__":
    game = RummyGame(num_players=2)
    game.play_game()