"""
Args:
    board: A 2D list representing the Sudoku board.

Returns:
    A tuple (row, col) of the empty cell, or None if no empty cells are found.
"""
for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            return (row, col)
return None