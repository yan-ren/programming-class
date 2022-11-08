public class PrivateOverride {
    public void f(int x) {
        System.out.println("privateOverride");
    }

    public static void main(String[] args) {
        // PrivateOverride po = new Derived();
        // po.f(1);
        // po.f(1.0);

        Parent p1 = new Parent();
        Child c = new Child();
        c.hello();
        p1.hello();
        Parent p2 = new Child();
        p2.hello();
    }
}

class Parent {
    public static void classMethod() {
        System.out.println("ClassMethod in Parent");
    }

    public void instanceMethod() {
        System.out.println("InstanceMethod in Parent");
    }

    public void hello() {
        System.out.println("Hello from parent call classMethod");
        classMethod();
    }
}

class Child extends Parent {
    public static void classMethod() {
        System.out.println("ClassMethod in Child");
    }

    public void instanceMethod() {
        System.out.println("InstanceMethod in Child");
    }
}