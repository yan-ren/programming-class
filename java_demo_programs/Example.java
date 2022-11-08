import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

public class Example {
    public static void main(String[] args) {
        // int[] test = { 5, 4, 3, 2, 1 };
        // selectionSort(test);
        // System.out.println(Arrays.toString(test));

        // A a = new A();
        // a.print();

        // A a = new B();
        // a.print();
        // B b = (B) a;
        // b.print1();

        // C c = new D();
        // c.print();

        // B b = new A();
        // b.print1();

        // B b = new B();
        // A a = (B) b;

        // A a = new A();
        // B b = (B) a;
        // b.print1();

        int[] myNumbers = { 1, 2, 3 };
        System.out.println(myNumbers[10]);

        try {
            FileReader file = new FileReader("C:\\test\\a.txt");

            // Creating object as one of ways of taking input
            BufferedReader fileInput = new BufferedReader(file);

            // Printing first 3 lines of file "C:\test\a.txt"
            for (int counter = 0; counter < 3; counter++)
                System.out.println(fileInput.readLine());

            // Closing file connections
            // using close() method
            fileInput.close();
        } catch (Exception e) {

        }
    }

    //
    public static void selectionSort(int[] arr) {
        for (int j = 0; j < arr.length - 1; j++) {
            int smallest = j;
            int i;
            for (i = j + 1; i < arr.length; i++) {
                if (arr[i] < arr[smallest]) {
                    smallest = i;
                }
            }

            // swap
            int tmp = arr[j];
            arr[j] = arr[smallest];
            arr[smallest] = tmp;
        }
    }
}

interface C {
    public void print();
}

class D implements C {
    public void print() {
        System.out.println("this is class D");
    }
}

class A {

    public void print() {
        System.out.println("this is class A");
    }
}

class B extends A {
    public void print() {
        System.out.println("this is class B");
    }

    public void print1() {
        System.out.println("this is class B: print1");
    }
}