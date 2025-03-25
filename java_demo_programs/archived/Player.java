package archived;

public class Player {
    private int x;
    private int y;

    public Player(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getX() {
        return this.x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getY() {
        return this.y;
    }

    public void moveLeft(int move) {
        this.x -= move;
    }

    // public double distanceToOrigin() {
    // // Math.sqrt(a);
    // Math.pow(2, 3);
    // }

    public static void main(String[] args) {
        Animal animal = new Pig();
        animal.animalSound();

        Pig pig = new Pig();

    }
}

/*
 * An interface is to group related methos with empty bodies
 */

// interface archived.Animal {
//     // abstract function/method
//     public abstract void animalSound();

//     public void run();
// }

// interface SecondInterface {

// }

// class archived.Pig implements archived.Animal, SecondInterface {
// public void animalSound() {
// System.out.println("pig sound");
// }

// public void run() {
// System.out.println("pig run");
// }

// public void print() {
// System.out.println("pront");
// }
// }

abstract class Animal {
    public String name;

    public abstract void animalSound();

    public void sleep() {

    }
}

class Pig extends Animal {
    public void animalSound() {

    }
}