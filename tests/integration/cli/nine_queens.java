package tests.integration.cli;

public class nine_queens {
        private static final int N = 9;
    
        public static void main(String[] args) {
            int[][] board = new int[N][N];
            if (solveNQueens(board, 0)) {
                printBoard(board);
            } else {
                System.out.println("No solution exists.");
            }
        }
    
        private static boolean solveNQueens(int[][] board, int col) {
            if (col >= N) {
                return true; // All queens are placed
            }
    
            for (int row = 0; row < N; row++) {
                if (isSafe(board, row, col)) {
                    board[row][col] = 1; // Place queen
                    if (solveNQueens(board, col + 1)) {
                        return true;
                    }
                    board[row][col] = 0; // Backtrack
                }
            }
            return false; // No valid position found
        }
    
        private static boolean isSafe(int[][] board, int row, int col) {
            // Check this row on the left
            for (int i = 0; i < col; i++) {
                if (board[row][i] == 1) {
                    return false;
                }
            }
    
            // Check upper diagonal on the left
            for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
                if (board[i][j] == 1) {
                    return false;
                }
            }
    
            // Check lower diagonal on the left
            for (int i = row, j = col; i < N && j >= 0; i++, j--) {
                if (board[i][j] == 1) {
                    return false;
                }
            }
    
            return true;
        }
    
        private static void printBoard(int[][] board) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.print((board[i][j] == 1 ? "Q " : ". "));
                }
                System.out.println();
            }
        }
    
}
