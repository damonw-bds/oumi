import random

class DotsGame:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.horizontal_lines = [[False for _ in range(size - 1)] for _ in range(size)]
        self.vertical_lines = [[False for _ in range(size)] for _ in range(size - 1)]
        self.scores = {'User': 0, 'Computer': 0}

    def display_board(self):
        print("\nCurrent Board:")
        for i in range(self.size):
            # Print horizontal lines
            for j in range(self.size - 1):
                print("o", end="")
                print("---" if self.horizontal_lines[i][j] else "   ", end="")
            print("o")
            # Print vertical lines and spaces
            if i < self.size - 1:
                for j in range(self.size):
                    print("|   " if self.vertical_lines[i][j] else "    ", end="")
                print()
        print()

    def is_valid_move(self, line_type, row, col):
        if line_type == 'H':
            return 0 <= row < self.size and 0 <= col < self.size - 1 and not self.horizontal_lines[row][col]
        elif line_type == 'V':
            return 0 <= row < self.size - 1 and 0 <= col < self.size and not self.vertical_lines[row][col]
        return False

    def make_move(self, line_type, row, col, player):
        if line_type == 'H':
            self.horizontal_lines[row][col] = True
        elif line_type == 'V':
            self.vertical_lines[row][col] = True

        # Check if a box is completed
        completed_boxes = self.check_boxes()
        self.scores[player] += completed_boxes
        return completed_boxes > 0

    def check_boxes(self):
        completed_boxes = 0
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if (self.horizontal_lines[i][j] and self.horizontal_lines[i + 1][j] and
                        self.vertical_lines[i][j] and self.vertical_lines[i][j + 1]):
                    completed_boxes += 1
        return completed_boxes

    def computer_move(self):
        while True:
            line_type = random.choice(['H', 'V'])
            row = random.randint(0, self.size - 2 if line_type == 'V' else self.size - 1)
            col = random.randint(0, self.size - 2 if line_type == 'H' else self.size - 1)
            if self.is_valid_move(line_type, row, col):
                print(f"Computer chooses: {line_type} {row} {col}")
                self.make_move(line_type, row, col, 'Computer')
                break

    def play(self):
        print("Welcome to the game of Dots!")
        print("Take turns connecting dots to form boxes.")
        print("Enter your move as: H/V row col (e.g., H 0 1 for a horizontal line at row 0, column 1).")
        while True:
            self.display_board()
            print(f"Scores: User - {self.scores['User']}, Computer - {self.scores['Computer']}")
            # User's turn
            while True:
                move = input("Your move (H/V row col): ").split()
                if len(move) == 3 and move[0] in ['H', 'V'] and move[1].isdigit() and move[2].isdigit():
                    line_type, row, col = move[0], int(move[1]), int(move[2])
                    if self.is_valid_move(line_type, row, col):
                        self.make_move(line_type, row, col, 'User')
                        break
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Try again.")

            # Check if the game is over
            if sum(self.scores.values()) == (self.size - 1) ** 2:
                break

            # Computer's turn
            self.computer_move()

        # Game over
        self.display_board()
        print(f"Final Scores: User - {self.scores['User']}, Computer - {self.scores['Computer']}")
        if self.scores['User'] > self.scores['Computer']:
            print("Congratulations! You win!")
        elif self.scores['User'] < self.scores['Computer']:
            print("Computer wins! Better luck next time.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = DotsGame(size=4)
    game.play()