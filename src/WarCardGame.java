import java.util.*;

public class WarCardGame {

    public static void main(String[] args) {
        // Initialize the deck and shuffle it
        List<Card> deck = createDeck();
        Collections.shuffle(deck);

        // Split the deck between two players
        Queue<Card> player1Deck = new LinkedList<>(deck.subList(0, 26));
        Queue<Card> player2Deck = new LinkedList<>(deck.subList(26, 52));

        // Play the game
        while (!player1Deck.isEmpty() && !player2Deck.isEmpty()) {
            playRound(player1Deck, player2Deck);
        }

        // Determine the winner
        if (player1Deck.isEmpty()) {
            System.out.println("Player 2 wins the game!");
        } else {
            System.out.println("Player 1 wins the game!");
        }
    }

    private static List<Card> createDeck() {
        List<Card> deck = new ArrayList<>();
        String[] suits = {"Hearts", "Diamonds", "Clubs", "Spades"};
        String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"};
        for (String suit : suits) {
            for (int i = 0; i < ranks.length; i++) {
                deck.add(new Card(ranks[i], suit, i + 2));
            }
        }
        return deck;
    }

    private static void playRound(Queue<Card> player1Deck, Queue<Card> player2Deck) {
        Card player1Card = player1Deck.poll();
        Card player2Card = player2Deck.poll();

        System.out.println("Player 1 plays: " + player1Card);
        System.out.println("Player 2 plays: " + player2Card);

        if (player1Card.getValue() > player2Card.getValue()) {
            System.out.println("Player 1 wins the round!");
            player1Deck.add(player1Card);
            player1Deck.add(player2Card);
        } else if (player1Card.getValue() < player2Card.getValue()) {
            System.out.println("Player 2 wins the round!");
            player2Deck.add(player1Card);
            player2Deck.add(player2Card);
        } else {
            System.out.println("It's a tie! War!");
            handleWar(player1Deck, player2Deck, player1Card, player2Card);
        }
    }

    private static void handleWar(Queue<Card> player1Deck, Queue<Card> player2Deck, Card player1Card, Card player2Card) {
        List<Card> warPile = new ArrayList<>();
        warPile.add(player1Card);
        warPile.add(player2Card);

        for (int i = 0; i < 3; i++) {
            if (!player1Deck.isEmpty()) {
                warPile.add(player1Deck.poll());
            }
            if (!player2Deck.isEmpty()) {
                warPile.add(player2Deck.poll());
            }
        }

        if (player1Deck.isEmpty() || player2Deck.isEmpty()) {
            return;
        }

        Card newPlayer1Card = player1Deck.poll();
        Card newPlayer2Card = player2Deck.poll();

        System.out.println("Player 1 plays: " + newPlayer1Card);
        System.out.println("Player 2 plays: " + newPlayer2Card);

        if (newPlayer1Card.getValue() > newPlayer2Card.getValue()) {
            System.out.println("Player 1 wins the war!");
            player1Deck.addAll(warPile);
            player1Deck.add(newPlayer1Card);
            player1Deck.add(newPlayer2Card);
        } else if (newPlayer1Card.getValue() < newPlayer2Card.getValue()) {
            System.out.println("Player 2 wins the war!");
            player2Deck.addAll(warPile);
            player2Deck.add(newPlayer1Card);
            player2Deck.add(newPlayer2Card);
        } else {
            System.out.println("The war continues!");
            handleWar(player1Deck, player2Deck, newPlayer1Card, newPlayer2Card);
        }
    }
}

class Card {
    private final String rank;
    private final String suit;
    private final int value;

    public Card(String rank, String suit, int value) {
        this.rank = rank;
        this.suit = suit;
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    @Override
    public String toString() {
        return rank + " of " + suit;
    }
}