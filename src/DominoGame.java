import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DominoGame {
    private final List<Domino> dominoes;
    private final List<Player> players;
    private final List<Domino> board;

    public DominoGame() {
        this.dominoes = new ArrayList<>();
        this.players = new ArrayList<>();
        this.board = new ArrayList<>();
        initializeDominoes();
    }

    private void initializeDominoes() {
        for (int i = 0; i <= 6; i++) {
            for (int j = i; j <= 6; j++) {
                dominoes.add(new Domino(i, j));
            }
        }
        Collections.shuffle(dominoes);
    }

    public void addPlayer(String name) {
        players.add(new Player(name));
    }

    public void dealDominoes() {
        int dominoesPerPlayer = 7;
        for (Player player : players) {
            for (int i = 0; i < dominoesPerPlayer; i++) {
                if (!dominoes.isEmpty()) {
                    player.addDomino(dominoes.remove(0));
                }
            }
        }
    }

    public void playGame() {
        if (players.isEmpty()) {
            System.out.println("No players in the game.");
            return;
        }

        board.add(dominoes.remove(0)); // Start with the first domino on the board
        System.out.println("Starting board: " + board);

        int currentPlayerIndex = 0;
        while (true) {
            Player currentPlayer = players.get(currentPlayerIndex);
            System.out.println(currentPlayer.getName() + "'s turn.");

            boolean played = false;
            for (Domino domino : new ArrayList<>(currentPlayer.getHand())) {
                if (domino.matches(board.get(0).getLeft()) || domino.matches(board.get(board.size() - 1).getRight())) {
                    currentPlayer.playDomino(domino, board.get(0).getLeft());
                    board.add(domino);
                    played = true;
                    System.out.println(currentPlayer.getName() + " played " + domino);
                    break;
                }
            }

            if (!played) {
                System.out.println(currentPlayer.getName() + " cannot play.");
            }

            if (currentPlayer.getHand().isEmpty()) {
                System.out.println(currentPlayer.getName() + " wins!");
                break;
            }

            currentPlayerIndex = (currentPlayerIndex + 1) % players.size();
        }
    }

    public static void main(String[] args) {
        DominoGame game = new DominoGame();
        game.addPlayer("Alice");
        game.addPlayer("Bob");
        game.dealDominoes();
        game.playGame();
    }
}