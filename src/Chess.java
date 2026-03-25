import java.util.Scanner;

public class Chess {

    private static final int BOARD_SIZE = 8;
    private static final char EMPTY = '.';
    private static final char PAWN = 'P';
    private static final char KING = 'K';

    private char[][] board;

    public Chess() {
        board = new char[BOARD_SIZE][BOARD_SIZE];
        initializeBoard();
    }

    private void initializeBoard() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                board[i][j] = EMPTY;
            }
        }
        // Place pawns
        for (int j = 0; j < BOARD_SIZE; j++) {
            board[1][j] = PAWN; // Player 1 pawns
            board[6][j] = PAWN; // Player 2 pawns
        }
        // Place kings
        board[0][4] = KING; // Player 1 king
        board[7][4] = KING; // Player 2 king
    }

    private void printBoard() {
        System.out.println("  0 1 2 3 4 5 6 7");
        for (int i = 0; i < BOARD_SIZE; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < BOARD_SIZE; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    private boolean isValidMove(int startX, int startY, int endX, int endY, char player) {
        if (endX < 0 || endX >= BOARD_SIZE || endY < 0 || endY >= BOARD_SIZE) {
            return false;
        }
        if (board[endX][endY] != EMPTY) {
            return false;
        }
        char piece = board[startX][startY];
        if (piece == PAWN) {
            int direction = (player == '1') ? 1 : -1;
            if (startX + direction == endX && startY == endY) {
                return true;
            }
        } else if (piece == KING) {
            if (Math.abs(startX - endX) <= 1 && Math.abs(startY - endY) <= 1) {
                return true;
            }
        }
        return false;
    }

    private void makeMove(int startX, int startY, int endX, int endY) {
        char piece = board[startX][startY];
        board[startX][startY] = EMPTY;
        board[endX][endY] = piece;
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        char currentPlayer = '1';
        while (true) {
            printBoard();
            System.out.println("Player " + currentPlayer + "'s turn.");
            System.out.print("Enter startX startY endX endY: ");
            int startX = scanner.nextInt();
            int startY = scanner.nextInt();
            int endX = scanner.nextInt();
            int endY = scanner.nextInt();

            if (isValidMove(startX, startY, endX, endY, currentPlayer)) {
                makeMove(startX, startY, endX, endY);
                currentPlayer = (currentPlayer == '1') ? '2' : '1';
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
    }

    public static void main(String[] args) {
        Chess game = new Chess();
        game.play();
    }
}