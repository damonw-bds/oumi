import java.util.Scanner;

public class Checkers {

    private static final int BOARD_SIZE = 8;
    private static final char EMPTY = '.';
    private static final char PLAYER_ONE = 'X';
    private static final char PLAYER_TWO = 'O';

    private char[][] board;

    public Checkers() {
        board = new char[BOARD_SIZE][BOARD_SIZE];
        initializeBoard();
    }

    private void initializeBoard() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                if ((i + j) % 2 != 0) {
                    if (i < 3) {
                        board[i][j] = PLAYER_ONE;
                    } else if (i > 4) {
                        board[i][j] = PLAYER_TWO;
                    } else {
                        board[i][j] = EMPTY;
                    }
                } else {
                    board[i][j] = EMPTY;
                }
            }
        }
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
        int direction = (player == PLAYER_ONE) ? 1 : -1;
        if (Math.abs(startX - endX) == 1 && endY - startY == direction) {
            return true;
        }
        if (Math.abs(startX - endX) == 2 && Math.abs(endY - startY) == 2) {
            int midX = (startX + endX) / 2;
            int midY = (startY + endY) / 2;
            if (board[midX][midY] != EMPTY && board[midX][midY] != player) {
                return true;
            }
        }
        return false;
    }

    private void makeMove(int startX, int startY, int endX, int endY, char player) {
        board[startX][startY] = EMPTY;
        board[endX][endY] = player;
        if (Math.abs(startX - endX) == 2) {
            int midX = (startX + endX) / 2;
            int midY = (startY + endY) / 2;
            board[midX][midY] = EMPTY;
        }
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        char currentPlayer = PLAYER_ONE;
        while (true) {
            printBoard();
            System.out.println("Player " + currentPlayer + "'s turn.");
            System.out.print("Enter startX startY endX endY: ");
            int startX = scanner.nextInt();
            int startY = scanner.nextInt();
            int endX = scanner.nextInt();
            int endY = scanner.nextInt();

            if (isValidMove(startX, startY, endX, endY, currentPlayer)) {
                makeMove(startX, startY, endX, endY, currentPlayer);
                currentPlayer = (currentPlayer == PLAYER_ONE) ? PLAYER_TWO : PLAYER_ONE;
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
    }

    public static void main(String[] args) {
        Checkers game = new Checkers();
        game.play();
    }
}