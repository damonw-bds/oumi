import random

def create_deck():
    """
    Create a deck of cards with one Queen removed (Old Maid).
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    deck.remove('Queen of Spades')  # Remove one Queen to create the Old Maid
    return deck

def deal_cards(deck, num_players):
    """
    Shuffle and deal cards to players.
    """
    random.shuffle(deck)
    hands = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        hands[i % num_players].append(card)
    return hands

def remove_pairs(hand):
    """
    Remove all pairs from a player's hand.
    """
    hand.sort()
    i = 0
    while i < len(hand) - 1:
        if hand[i][:-1] == hand[i + 1][:-1]:  # Compare ranks
            hand.pop(i)
            hand.pop(i)  # Remove the pair
        else:
            i += 1
    random.shuffle(hand)  # Shuffle the hand after removing pairs
    return hand

def play_turn(player_hand, next_player_hand):
    """
    Simulate a player's turn by drawing a card from the next player's hand.
    """
    if next_player_hand:
        drawn_card = random.choice(next_player_hand)
        next_player_hand.remove(drawn_card)
        player_hand.append(drawn_card)
        player_hand = remove_pairs(player_hand)
    return player_hand, next_player_hand

def main():
    print("Welcome to Old Maid!")
    num_players = int(input("Enter the number of players (2 or more): "))
    if num_players < 2:
        print("You need at least 2 players to play Old Maid.")
        return

    # Setup the game
    deck = create_deck()
    hands = deal_cards(deck, num_players)
    hands = [remove_pairs(hand) for hand in hands]

    # Play the game
    while True:
        for i in range(num_players):
            if len(hands[i]) == 0:
                continue  # Skip players with no cards

            next_player = (i + 1) % num_players
            while len(hands[next_player]) == 0:
                next_player = (next_player + 1) % num_players

            print(f"Player {i + 1}'s turn.")
            hands[i], hands[next_player] = play_turn(hands[i], hands[next_player])

            if len(hands[i]) == 0:
                print(f"Player {i + 1} is out of cards!")

            # Check for a winner
            active_players = [hand for hand in hands if len(hand) > 0]
            if len(active_players) == 1:
                loser = hands.index(active_players[0]) + 1
                print(f"Player {loser} is the Old Maid!")
                return

if __name__ == "__main__":
    main()