import random

class Pawn:
    def __init__(self, player, id):
        self.player = player
        self.id = id
        self.position = -1  # -1 means start

class Player:
    def __init__(self, name):
        self.name = name
        self.pawns = [Pawn(self, i) for i in range(4)]

class SorryGame:
    def __init__(self, players):
        self.board_size = 60
        self.players = [Player(name) for name in players]
        self.deck = self.init_deck()
        self.current_player_idx = 0

    def init_deck(self):
        # Represents Sorry! cards
        deck = [1]*5 + [2]*4 + [3]*4 + [4]*4 + [5]*4 + [7]*4 + [8]*4 + [10]*4 + [11]*4 + ['Sorry']*4
        random.shuffle(deck)
        return deck

    def draw_card(self):
        if not self.deck:
            self.deck = self.init_deck()
        return self.deck.pop(random.randint(0, len(self.deck)-1))

    def next_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def move_pawn(self, pawn, steps):
        if pawn.position == -1 and steps != 1 and steps != 2:
            return False  # Only 1 or 2 can bring pawn out
        elif pawn.position == -1:
            pawn.position = 0
        else:
            pawn.position = min(self.board_size, pawn.position + steps)
        # "Sorry!" card only: send opponent's pawn home
        return True

    def is_winner(self, player):
        return all(p.position == self.board_size for p in player.pawns)

    def play(self):
        print("Starting Sorry!")
        while True:
            player = self.players[self.current_player_idx]
            card = self.draw_card()
            print(f"{player.name}'s turn. Drew {card}.")
            movable = [p for p in player.pawns if (p.position != self.board_size)]
            if not movable:
                print(f"{player.name} has no movable pawns.")
                self.next_player()
                continue
            pawn = movable[0]  # Pick first movable pawn for simplicity
            if card == 'Sorry':
                # Find first opponent pawn not home
                for opp in self.players:
                    if opp == player:
                        continue
                    target = [p for p in opp.pawns if p.position not in (-1, self.board_size)]
                    if target:
                        p = target[0]
                        print(f"{player.name} bumps {opp.name}'s pawn {p.id} back to start!")
                        p.position = -1
                        pawn.position = 0
                        break
                else:
                    print("No opponent pawn to bump.")
            elif self.move_pawn(pawn, card):
                print(f"{player.name} moves pawn {pawn.id} to {pawn.position}")
            else:
                print(f"{player.name} can't move pawn {pawn.id} with a card {card}")
            if self.is_winner(player):
                print(f"{player.name} wins!")
                break
            self.next_player()

if __name__ == "__main__":
    SorryGame(["Alice", "Bob"]).play()