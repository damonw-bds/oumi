import numpy as np

ROWS = 6
COLUMNS = 7

def create_board():
    """Creates an empty Connect Four board."""
    return np.zeros((ROWS, COLUMNS), dtype=int)

def drop_piece(board, row, col, piece):
    """Drops a piece into the board."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Checks if a column has space for a piece."""
    return board[ROWS - 1][col] == 0

def get_next_open_row(board, col):
    """Finds the next open row in a column."""
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

def print_board(board):
    """Prints the board (flipped for correct orientation)."""
    print(np.flip(board, 0))

def winning_move(board, piece):
    """Checks if the given piece has a winning move."""
    # Check horizontal locations
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True

    return False

def play_game():
    """Main function to play Connect Four."""
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        # Ask for Player 1 input
        if turn == 0:
            col = int(input("Player 1, make your selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("Player 1 wins!")
                    game_over = True

        # Ask for Player 2 input
        else:
            col = int(input("Player 2, make your selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)

        turn += 1
        turn %= 2

if __name__ == "__main__":
    play_game()