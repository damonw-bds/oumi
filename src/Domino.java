public class Domino {
    private final int left;
    private final int right;

    public Domino(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public int getLeft() {
        return left;
    }

    public int getRight() {
        return right;
    }

    public boolean matches(int value) {
        return left == value || right == value;
    }

    @Override
    public String toString() {
        return "[" + left + "|" + right + "]";
    }
}