class FoxAndHounds:
    def __init__(self):
        self.board_size = 8
        self.board = [["." for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.hounds = [(0, 1), (0, 3), (0, 5), (0, 7)]  # Initial positions of hounds
        self.fox = (7, 0)  # Initial position of the fox
        self.turn = "fox"  # Fox starts the game
        self.setup_board()

    def setup_board(self):
        for hound in self.hounds:
            self.board[hound[0]][hound[1]] = "H"
        self.board[self.fox[0]][self.fox[1]] = "F"

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def move_hound(self, hound_index, new_position):
        if self.turn != "hounds":
            print("It's not the hounds' turn!")
            return False

        old_position = self.hounds[hound_index]
        if self.is_valid_hound_move(old_position, new_position):
            self.board[old_position[0]][old_position[1]] = "."
            self.hounds[hound_index] = new_position
            self.board[new_position[0]][new_position[1]] = "H"
            self.turn = "fox"
            return True
        else:
            print("Invalid move for hound!")
            return False

    def move_fox(self, new_position):
        if self.turn != "fox":
            print("It's not the fox's turn!")
            return False

        old_position = self.fox
        if self.is_valid_fox_move(old_position, new_position):
            self.board[old_position[0]][old_position[1]] = "."
            self.fox = new_position
            self.board[new_position[0]][new_position[1]] = "F"
            self.turn = "hounds"
            return True
        else:
            print("Invalid move for fox!")
            return False

    def is_valid_hound_move(self, old_position, new_position):
        row_diff = new_position[0] - old_position[0]
        col_diff = abs(new_position[1] - old_position[1])
        return row_diff == 1 and col_diff == 1 and self.is_within_board(new_position) and self.board[new_position[0]][new_position[1]] == "."

    def is_valid_fox_move(self, old_position, new_position):
        row_diff = abs(new_position[0] - old_position[0])
        col_diff = abs(new_position[1] - old_position[1])
        return row_diff == 1 and col_diff == 1 and self.is_within_board(new_position) and self.board[new_position[0]][new_position[1]] == "."

    def is_within_board(self, position):
        return 0 <= position[0] < self.board_size and 0 <= position[1] < self.board_size

    def check_winner(self):
        if self.fox[0] == 0:
            return "Fox wins!"
        for hound in self.hounds:
            if self.is_valid_fox_move(self.fox, hound):
                return None
        return "Hounds win!"

    def play(self):
        self.print_board()
        while True:
            if self.turn == "fox":
                print("Fox's turn!")
                new_row = int(input("Enter new row for fox: "))
                new_col = int(input("Enter new column for fox: "))
                if self.move_fox((new_row, new_col)):
                    winner = self.check_winner()
                    if winner:
                        print(winner)
                        break
            else:
                print("Hounds' turn!")
                hound_index = int(input("Enter hound index (0-3): "))
                new_row = int(input("Enter new row for hound: "))
                new_col = int(input("Enter new column for hound: "))
                if self.move_hound(hound_index, (new_row, new_col)):
                    winner = self.check_winner()
                    if winner:
                        print(winner)
                        break
            self.print_board()


if __name__ == "__main__":
    game = FoxAndHounds()
    game.play()