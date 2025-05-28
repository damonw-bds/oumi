import random

# Define suits and ranks
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

    def play_card(self, card):
        self.hand.remove(card)
        return card

    def has_suit(self, suit):
        return any(card.suit == suit for card in self.hand)

class HeartsGame:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.scores = {player.name: 0 for player in self.players}
        self.deal_cards()

    def deal_cards(self):
        while self.deck.cards:
            for player in self.players:
                if self.deck.cards:
                    player.hand.append(self.deck.deal())

    def play_round(self):
        print("\nStarting a new round!")
        trick = []
        lead_suit = None

        for player in self.players:
            print(f"{player.name}'s hand: {[str(card) for card in player.hand]}")
            if lead_suit:
                valid_cards = [card for card in player.hand if card.suit == lead_suit]
                if not valid_cards:
                    valid_cards = player.hand
            else:
                valid_cards = player.hand

            chosen_card = random.choice(valid_cards)  # Simplified: Random card selection
            print(f"{player.name} plays {chosen_card}")
            trick.append((player, chosen_card))
            player.play_card(chosen_card)

            if not lead_suit:
                lead_suit = chosen_card.suit

        winner = self.determine_trick_winner(trick, lead_suit)
        print(f"{winner.name} wins the trick!")
        self.update_scores(trick)

    def determine_trick_winner(self, trick, lead_suit):
        lead_cards = [card for player, card in trick if card.suit == lead_suit]
        winning_card = max(lead_cards, key=lambda card: card.value())
        for player, card in trick:
            if card == winning_card:
                return player

    def update_scores(self, trick):
        for _, card in trick:
            if card.suit == 'Hearts':
                self.scores[_] += 1
            elif card.suit == 'Queen' and card.rank == 'Spades':
                self.scores[+=13]