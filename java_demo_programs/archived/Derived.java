package archived;

public class Derived extends PrivateOverride {
    public void f(double x) { // this method is never run.
        System.out.println("derived");
    }
}