Args:
    board: A 2D list representing the Sudoku board.

Returns:
    A tuple (row, col) representing the location of the empty cell,
    or None if no empty cell is found.
"""
for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            return (row, col)
return None