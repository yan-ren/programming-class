package archived;

import java.util.ArrayList;
import java.util.List;

// public interface archived.ApplePredicate extends FruitPredicate {
//     // abstract function
//     abstract boolean test2();
// }

// interface FruitPredicate {
//     boolean test1();
// }

// class AppleImpl implements archived.ApplePredicate {

//     // abstract test3();

//     public boolean test1() {
//         return false;
//     }

//     public boolean test2() {
//         return true;
//     }
// }

// // abstract class
// /*
//  * abstract class can have abstract/non-abstract method inside
//  * abstract class cannot be used to create object, it must be inherited from another class
//  */
// abstract class AppleAbstract {
//     public abstract void test3();

//     public void test4() {

//     }
// }

// class archived.Apple extends AppleAbstract {

//     @Override
//     public void test3() {
//         // TODO Auto-generated method stub

//     }

// }

public class FunctionalProgramming {

    // filter green apples
    public static List<Apple> filterGreenApples(List<Apple> inventory) {
        List<Apple> result = new ArrayList<>();
        for (Apple apple : inventory) {
            if (apple.getColor().equals("green")) {
                result.add(apple);
            }
        }

        return result;
    }

    // filter by abitrary color
    public static List<Apple> filterApplesByColor(List<Apple> inventory,
            String color) {
        List<Apple> result = new ArrayList<>();
        for (Apple apple : inventory) {
            if (apple.getColor().equals(color)) {
                result.add(apple);
            }
        }
        return result;
    }

    // filter by weight
    public static List<Apple> filterApplesByWeight(List<Apple> inventory,
            int weight) {
        List<Apple> result = new ArrayList<>();
        for (Apple apple : inventory) {
            if (apple.getWeight() > weight) {
                result.add(apple);
            }
        }
        return result;
    }

    // filter by weight or color?
    // when flag is true, filter by color
    // when flag is false, filter by weight
    // public static List<archived.Apple> filterApples(List<archived.Apple> apples, String color, int
    // weight, boolean flag) {
    // List<archived.Apple> result = new ArrayList<>();
    // for (archived.Apple apple : apples) {
    // if (flag) {
    // if (apple.getColor().equals(color)) {
    // result.add(apple);
    // }
    // } else {
    // if (apple.getWeight() > weight) {
    // result.add(apple);
    // }
    // }
    // }

    // return result;
    // }

    public static List<Apple> filterApples(List<Apple> apples, ApplePredicate p) {
        List<Apple> result = new ArrayList<>();
        for (Apple apple : apples) {
            if (p.test(apple)) {
                result.add(apple);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        List<Apple> list = new ArrayList<>();
        list.add(new Apple("red", 150));
        list.add(new Apple("red", 120));
        list.add(new Apple("red", 100));

        // filterApples(list, new archived.AppleWeightPredicate());

        // anonymous class
        filterApples(list, new ApplePredicate() {
            public boolean test(Apple apple) {
                return apple.getWeight() > 100;
            }
        });

        // functional programming -> lambda expression
        // object oriented programming -> class
        // List<archived.Apple> result = filterApples(list, (archived.Apple apple) -> apple.getWeight() >
        // 100);

        // another example
        // anonymous class
        // sort the list of apple
        System.out.println(list);

        // list.sort(new Comparator<archived.Apple>() {
        // public int compare(archived.Apple a1, archived.Apple a2) {
        // if (a1.getWeight() > a2.getWeight()) {
        // return 1;
        // } else if (a1.getWeight() < a2.getWeight()) {
        // return -1;
        // } else {
        // return 0;
        // }
        // }
        // });

        // System.out.println(list);

        // lambda expression
        list.sort((Apple a1, Apple a2) -> {
            if (a1.getWeight() > a2.getWeight()) {
                return 1;
            } else if (a1.getWeight() < a2.getWeight()) {
                return -1;
            } else {
                return 0;
            }
        });

        System.out.println(list);
    }
}

interface ApplePredicate {
    boolean test(Apple apple);
}

class AppleWeightPredicate implements ApplePredicate {
    public boolean test(Apple apple) {
        return apple.getWeight() > 100;
    }
}

class AppleGreenColorPredicate implements ApplePredicate {
    public boolean test(Apple apple) {
        return apple.getColor().equals("green");
    }
}

class Apple {
    private String color;
    private int weight;

    public Apple(String color, int weight) {
        this.color = color;
        this.weight = weight;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return "{" +
                " color='" + getColor() + "'" +
                ", weight='" + getWeight() + "'" +
                "}";
    }
}
