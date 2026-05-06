import random

def create_deck():
    """Create a deck of cards with one Queen removed (Old Maid)."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    deck.remove('Queen of Spades')  # Remove one Queen to create the Old Maid
    return deck

def deal_cards(deck, num_players):
    """Shuffle and deal cards to players."""
    random.shuffle(deck)
    hands = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        hands[i % num_players].append(card)
    return hands

def remove_pairs(hand):
    """Remove pairs from a player's hand."""
    hand.sort()
    i = 0
    while i < len(hand) - 1:
        if hand[i].split()[0] == hand[i + 1].split()[0]:  # Compare ranks
            del hand[i:i + 2]  # Remove the pair
        else:
            i += 1
    random.shuffle(hand)  # Shuffle the hand after removing pairs
    return hand

def play_turn(player_hand, next_player_hand):
    """Player draws a card from the next player's hand."""
    if next_player_hand:
        drawn_card = random.choice(next_player_hand)
        next_player_hand.remove(drawn_card)
        player_hand.append(drawn_card)
        player_hand = remove_pairs(player_hand)
    return player_hand, next_player_hand

def main():
    print("Welcome to Old Maid!")
    num_players = int(input("Enter the number of players (2-6): "))
    if num_players < 2 or num_players > 6:
        print("Invalid number of players. Exiting.")
        return

    # Setup game
    deck = create_deck()
    hands = deal_cards(deck, num_players)
    hands = [remove_pairs(hand) for hand in hands]

    # Game loop
    current_player = 0
    while True:
        print(f"\nPlayer {current_player + 1}'s turn.")
        print(f"Your hand: {hands[current_player]}")

        # Find the next player with cards
        next_player = (current_player + 1) % num_players
        while not hands[next_player]:
            next_player = (next_player + 1) % num_players
            if next_player == current_player:
                break

        if next_player == current_player:
            print(f"Player {current_player + 1} is the winner!")
            break

        print(f"Drawing a card from Player {next_player + 1}.")
        hands[current_player], hands[next_player] = play_turn(hands[current_player], hands[next_player])

        # Check if the current player is out of cards
        if not hands[current_player]:
            print(f"Player {current_player + 1} is out of cards!")
        
        # Move to the next player
        current_player = next_player

        # Check if only one player has cards left (Old Maid)
        active_players = [i for i in range(num_players) if hands[i]]
        if len(active_players) == 1:
            print(f"Player {active_players[0] + 1} is the Old Maid!")
            break

if __name__ == "__main__":
    main()