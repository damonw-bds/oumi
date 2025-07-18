# Interactive Hair Styling Game with Voting and ASCII Art

import random

# ASCII art for each style
ASCII_ART = {
    "Short": r"""
     __
    |  |
    |__|
    """,
    "Long": r"""
     __
    |  |
    |  |
    |  |
    |__|
    """,
    "Curly": r"""
    ~~~
    ( )
    ~~~
    """,
    "Straight": r"""
    |||
    |||
    |||
    """,
    "Braided": r"""
    }{
    }{
    }{
    """
}

STYLES = list(ASCII_ART.keys())
COLORS = ["Blonde", "Brown", "Black", "Red", "Blue"]

def get_choice(options, prompt):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return options[choice]

def show_dew(style, color):
    print(f"\n{color} {style} hair:")
    print(ASCII_ART[style])

def play_game(num_players=2):
    dews = []
    for i in range(num_players):
        print(f"\nPlayer {i+1}:")
        style = get_choice(STYLES, "Choose a hairstyle:")
        color = get_choice(COLORS, "Choose a hair color:")
        show_dew(style, color)
        dews.append((style, color))

    print("\nVote for the best dew!")
    for idx, (style, color) in enumerate(dews, 1):
        print(f"{idx}. {color} {style}")
        print(ASCII_ART[style])

    votes = [0] * num_players
    for voter in range(num_players):
        vote = int(input(f"Player {voter+1}, vote for your favorite dew (1-{num_players}): ")) - 1
        votes[vote] += 1

    winner = votes.index(max(votes))
    print(f"\nThe winning dew is: {COLORS[winner]} {STYLES[winner]}!")
    print(ASCII_ART[STYLES[winner]])

if __name__ == "__main__":
    num_players = int(input("How many players? (2-4): "))
    play_game(num_players)