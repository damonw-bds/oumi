class Checkers:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "X"  # Player X starts the game

    def create_board(self):
        """Create an 8x8 board with initial positions for checkers."""
        board = [[" " for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = "O"  # Player O's pieces
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = "X"  # Player X's pieces
        return board

    def print_board(self):
        """Print the current state of the board."""
        print("  " + " ".join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))
        print()

    def is_valid_move(self, start, end):
        """Check if a move is valid."""
        start_row, start_col = start
        end_row, end_col = end

        # Ensure the move is within bounds
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # Ensure the start position has the current player's piece
        if self.board[start_row][start_col] != self.current_player:
            return False

        # Ensure the end position is empty
        if self.board[end_row][end_col] != " ":
            return False

        # Check for valid movement (diagonal move)
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        if self.current_player == "X" and row_diff == -1 and col_diff == 1:
            return True
        if self.current_player == "O" and row_diff == 1 and col_diff == 1:
            return True

        # Check for valid jump (capture)
        if abs(row_diff) == 2 and col_diff == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            if self.board[mid_row][mid_col] in ("X", "O") and self.board[mid_row][mid_col] != self.current_player:
                return True

        return False

    def make_move(self, start, end):
        """Make a move on the board."""
        if not self.is_valid_move(start, end):
            print("Invalid move. Try again.")
            return False

        start_row, start_col = start
        end_row, end_col = end

        # Move the piece
        self.board[end_row][end_col] = self.current_player
        self.board[start_row][start_col] = " "

        # Check for and remove captured piece
        if abs(end_row - start_row) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            self.board[mid_row][mid_col] = " "

        # Switch players
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def has_winner(self):
        """Check if there is a winner."""
        x_pieces = sum(row.count("X") for row in self.board)
        o_pieces = sum(row.count("O") for row in self.board)
        if x_pieces == 0:
            return "O"
        if o_pieces == 0:
            return "X"
        return None

    def play(self):
        """Main game loop."""
        while True:
            self.print_board()
            winner = self.has_winner()
            if winner:
                print(f"Player {winner} wins!")
                break

            print(f"Player {self.current_player}'s turn.")
            try:
                start = tuple(map(int, input("Enter the start position (row col): ").split()))
                end = tuple(map(int, input("Enter the end position (row col): ").split()))
                self.make_move(start, end)
            except ValueError:
                print("Invalid input. Please enter row and column as numbers.")


if __name__ == "__main__":
    game = Checkers()
    game.play()