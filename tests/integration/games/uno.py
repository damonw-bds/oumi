import random

# Define the Uno card deck
COLORS = ["Red", "Yellow", "Green", "Blue"]
VALUES = [str(i) for i in range(0, 10)] + ["Skip", "Reverse", "Draw Two"]
SPECIAL_CARDS = ["Wild", "Wild Draw Four"]

def create_deck():
    """Create a standard Uno deck."""
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append(f"{color} {value}")
            if value != "0":  # Each non-zero card appears twice
                deck.append(f"{color} {value}")
    for special in SPECIAL_CARDS:
        deck.extend([special] * 4)  # Each special card appears 4 times
    random.shuffle(deck)
    return deck

class UnoGame:
    def __init__(self, num_players):
        self.deck = create_deck()
        self.players = {f"Player {i+1}": [] for i in range(num_players)}
        self.discard_pile = []
        self.current_player = 0
        self.direction = 1  # 1 for clockwise, -1 for counterclockwise
        self.initialize_game()

    def initialize_game(self):
        """Deal 7 cards to each player and start the discard pile."""
        for player in self.players:
            self.players[player] = [self.deck.pop() for _ in range(7)]
        self.discard_pile.append(self.deck.pop())
        print(f"Starting card: {self.discard_pile[-1]}")

    def draw_card(self, player):
        """Draw a card from the deck."""
        if not self.deck:
            self.deck = self.discard_pile[:-1]
            random.shuffle(self.deck)
            self.discard_pile = [self.discard_pile[-1]]
        self.players[player].append(self.deck.pop())

    def play_turn(self):
        """Play a single turn for the current player."""
        player_name = list(self.players.keys())[self.current_player]
        player_hand = self.players[player_name]
        top_card = self.discard_pile[-1]
        print(f"\n{player_name}'s turn. Top card: {top_card}")
        print(f"Your hand: {', '.join(player_hand)}")

        # Find playable cards
        playable_cards = [
            card for card in player_hand
            if card.split()[0] in top_card or card.split()[-1] in top_card or "Wild" in card
        ]

        if playable_cards:
            print(f"Playable cards: {', '.join(playable_cards)}")
            chosen_card = random.choice(playable_cards)  # Simulate a choice
            print(f"{player_name} plays {chosen_card}")
            player_hand.remove(chosen_card)
            self.discard_pile.append(chosen_card)

            # Handle special cards
            if "Wild" in chosen_card:
                chosen_color = random.choice(COLORS)  # Simulate choosing a color
                print(f"{player_name} chooses {chosen_color}")
                self.discard_pile[-1] = f"{chosen_color} {chosen_card.split()[-1]}"
            elif "Reverse" in chosen_card:
                self.direction *= -1
            elif "Skip" in chosen_card:
                self.current_player = (self.current_player + self.direction) % len(self.players)
            elif "Draw Two" in chosen_card:
                next_player = (self.current_player + self.direction) % len(self.players)
                next_player_name = list(self.players.keys())[next_player]
                self.draw_card(next_player_name)
                self.draw_card(next_player_name)
        else:
            print(f"{player_name} has no playable cards and draws a card.")
            self.draw_card(player_name)

        # Check for a winner
        if not player_hand:
            print(f"{player_name} wins!")
            return True

        # Move to the next player
        self.current_player = (self.current_player + self.direction) % len(self.players)
        return False

    def play_game(self):
        """Play the Uno game until there is a winner."""
        print("Starting Uno game!")
        while True:
            if self.play_turn():
                break

# Start the game with 2-4 players
if __name__ == "__main__":
    num_players = 4
    game = UnoGame(num_players)
    game.play_game()