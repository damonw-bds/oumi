import java.util.*;

public class Pinochle {
    private static final String[] SUITS = {"♠", "♥", "♦", "♣"};
    private static final String[] RANKS = {"9", "J", "Q", "K", "10", "A"}; // Pinochle deck ranks
    private static final int HAND_SIZE = 12; // Each player gets 12 cards

    public static void main(String[] args) {
        System.out.println("Welcome to Pinochle!");
        int numPlayers = getNumberOfPlayers();
        PinochleGame game = new PinochleGame(numPlayers);
        game.play();
    }

    private final Deck deck;
    private final List<Hand> players;
    private final int numPlayers;
    private final Scanner scanner;

    public PinochleGame(int numPlayers) {
        this.numPlayers = numPlayers;
        this.deck = new Deck();
        this.players = new ArrayList<>();
        this.scanner = new Scanner(System.in);
        dealHands();
    }

    private void dealHands() {
        for (int i = 0; i < numPlayers; i++) {
            players.add(new Hand(deck.deal(HAND_SIZE)));
        }
    }

    private void play() {
        // Game placeholder: distributing cards and displaying them
        System.out.println("\nDealing cards...");
        for (int i = 0; i < players.size(); i++) {
            System.out.println("Player " + (i + 1) + "'s Hand: " + players.get(i));
        }

        // Further phases like bidding, melding, and tricks can be added here
        System.out.println("\nGame logic not implemented yet. Enjoy your cards!");
    }

    private static int getNumberOfPlayers() {
        Scanner scanner = new Scanner(System.in);
        int players;
        do {
            System.out.print("Enter the number of players (2-4): ");
            players = scanner.nextInt();
        } while (players < 2 || players > 4);
        return players;
    }

    private static class Deck {
        private final List<String> cards;

        public Deck() {
            cards = new ArrayList<>();
            for (String suit : SUITS) {
                for (String rank : RANKS) {
                    cards.add(rank + suit);
                    cards.add(rank + suit); // Pinochle deck has double cards of each rank
                }
            }
            shuffle();
        }

        private void shuffle() {
            Collections.shuffle(cards);
        }

        public List<String> deal(int count) {
            List<String> hand = new ArrayList<>();
            for (int i = 0; i < count && !cards.isEmpty(); i++) {
                hand.add(cards.remove(cards.size() - 1));
            }
            return hand;
        }
    }

    private static class Hand {
        private final List<String> cards;

        public Hand(List<String> cards) {
            this.cards = cards;
        }

        @Override
        public String toString() {
            return String.join(", ", cards);
        }
    }
}