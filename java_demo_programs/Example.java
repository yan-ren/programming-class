import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

public class Example {

    public static void main(String[] args) {
        // canFly(new Owl());
        // canFly(new Eagle());
        // Owl o = new Owl();
        // FlyObject f = new Owl();

        Test t = new Test();
        t.a = 1;
        t.b = 2;

        Test.b = 2;

        Deque<Integer> queue = new LinkedList<>();
        queue.addFirst(null);
        queue.addLast(null);
    }

    // public static void canFly(Owl o) {
    // o.fly();
    // }

    // public static void canFly(Eagle e) {
    // e.fly();
    // }

    public static void canFly(FlyObject f) {
        f.fly();
    }
}

class Test {
    int a;
    static int b;
}

interface FlyObject {
    public void fly();
}

class Owl implements FlyObject {
    public void fly() {
        System.out.println("owl fly");
    }
}

class Eagle implements FlyObject {
    public void fly() {
        System.out.println("eagle fly");
    }
}
