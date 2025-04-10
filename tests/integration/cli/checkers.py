import random

# Initialize the board
def initialize_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'C'  # Computer pieces
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'U'  # User pieces
    return board

# Print the board
def print_board(board):
    print("  " + " ".join(str(i) for i in range(8)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

# Check if a move is valid
def is_valid_move(board, player, start, end):
    sx, sy = start
    ex, ey = end
    if ex < 0 or ex >= 8 or ey < 0 or ey >= 8:
        return False
    if board[ex][ey] != ' ':
        return False
    if player == 'U' and ex == sx - 1 and abs(ey - sy) == 1:
        return True
    if player == 'C' and ex == sx + 1 and abs(ey - sy) == 1:
        return True
    return False

# Make a move
def make_move(board, start, end):
    sx, sy = start
    ex, ey = end
    board[ex][ey] = board[sx][sy]
    board[sx][sy] = ' '

# Get all valid moves for a player
def get_valid_moves(board, player):
    moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] == player:
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if is_valid_move(board, player, (x, y), (x + dx, y + dy)):
                        moves.append(((x, y), (x + dx, y + dy)))
    return moves

# Computer's turn
def computer_turn(board):
    moves = get_valid_moves(board, 'C')
    if not moves:
        return False
    move = random.choice(moves)
    make_move(board, move[0], move[1])
    return True

# User's turn
def user_turn(board):
    moves = get_valid_moves(board, 'U')
    if not moves:
        return False
    print("Your turn! Enter your move as 'start_x start_y end_x end_y'")
    while True:
        try:
            move = input("Enter your move: ").strip().split()
            start = (int(move[0]), int(move[1]))
            end = (int(move[2]), int(move[3]))
            if is_valid_move(board, 'U', start, end):
                make_move(board, start, end)
                return True
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter coordinates as 'start_x start_y end_x end_y'")
    return False

# Main game loop
def play_checkers():
    board = initialize_board()
    print("Welcome to Checkers!")
    print_board(board)
    while True:
        if not user_turn(board):
            print("No valid moves left. You lose!")
            break
        print_board(board)
        if not computer_turn(board):
            print("No valid moves left for the computer. You win!")
            break
        print_board(board)

if __name__ == "__main__":
    play_checkers()