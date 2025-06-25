import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [f"{rank} of {suit}" for suit in SUITS for rank in RANKS]

def card_suit(card):
    return card.split(" of ")[1]

def card_rank(card):
    return card.split(" of ")[0]

def can_play(card, top_card, current_suit):
    return (card_rank(card) == '8' or card_suit(card) == current_suit or card_rank(card) == card_rank(top_card))

def display_hand(hand):
    for idx, card in enumerate(hand):
        print(f"{idx + 1}: {card}")

def choose_suit():
    while True:
        suit = input("Choose a suit (Hearts, Diamonds, Clubs, Spades): ").capitalize()
        if suit in SUITS:
            return suit
        print("Invalid suit.")

def crazy_eights():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [deck.pop() for _ in range(5)]
    cpu_hand = [deck.pop() for _ in range(5)]
    discard_pile = [deck.pop()]
    current_suit = card_suit(discard_pile[-1])
    current_player = "You"
    while True:
        print("\nTop card:", discard_pile[-1], f"({current_suit})")
        if current_player == "You":
            print("Your hand:")
            display_hand(player_hand)
            playable = [card for card in player_hand if can_play(card, discard_pile[-1], current_suit)]
            if not playable:
                if not deck:
                    print("Deck is empty. Skipping turn...")
                else:
                    drawn = deck.pop()
                    print("No playable card. Drawing a card:", drawn)
                    player_hand.append(drawn)
            else:
                while True:
                    try:
                        choice = int(input(f"Pick a card to play (1-{len(player_hand)}) or 0 to draw: "))
                        if choice == 0:
                            if not deck:
                                print("Deck is empty. Cannot draw. Skipping turn...")
                                break
                            drawn = deck.pop()
                            print("Drew:", drawn)
                            player_hand.append(drawn)
                            break
                        if 1 <= choice <= len(player_hand):
                            card = player_hand[choice - 1]
                            if can_play(card, discard_pile[-1], current_suit):
                                discard_pile.append(card)
                                player_hand.remove(card)
                                if card_rank(card) == '8':
                                    current_suit = choose_suit()
                                else:
                                    current_suit = card_suit(card)
                                break
                            else:
                                print("You cannot play that card. Try again.")
                    except ValueError:
                        print("Invalid input.")
            if not player_hand:
                print("You win!")
                break
            current_player = "CPU"
        else:
            playable = [card for card in cpu_hand if can_play(card, discard_pile[-1], current_suit)]
            if not playable:
                if deck:
                    cpu_hand.append(deck.pop())
                # Else: skip turn if deck is empty
            else:
                # Naive CPU: plays first valid card
                for card in playable:
                    cpu_hand.remove(card)
                    discard_pile.append(card)
                    print("CPU played:", card)
                    if card_rank(card) == '8':
                        current_suit = random.choice(SUITS)
                        print("CPU declared suit:", current_suit)
                    else:
                        current_suit = card_suit(card)
                    break
            if not cpu_hand:
                print("CPU wins!")
                break
            current_player = "You"

if __name__ == "__main__":
    crazy_eights()