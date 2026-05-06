import java.util.ArrayList;
import java.util.List;

public class Player {
    private final String name;
    private final List<Domino> hand;

    public Player(String name) {
        this.name = name;
        this.hand = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Domino> getHand() {
        return hand;
    }

    public void addDomino(Domino domino) {
        hand.add(domino);
    }

    public boolean playDomino(Domino domino, int value) {
        if (domino.matches(value)) {
            hand.remove(domino);
            return true;
        }
        return false;
    }

    public boolean hasPlayableDomino(int value) {
        for (Domino domino : hand) {
            if (domino.matches(value)) {
                return true;
            }
        }
        return false;
    }
}