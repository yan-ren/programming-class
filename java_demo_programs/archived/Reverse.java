package archived;

public class Reverse {
    public static void main(String[] args) {
        // int x = 1;
        // method1(x);
        // System.out.println(x);

        // int[] y = { 1 };
        // method1(y);
        // System.out.println(y[0]);

        int[] z = { 1, 2, 3 };
        reverse(z);
        for (int i = 0; i < z.length; i++) {
            System.out.println(z[i]);
        }
    }

    public static void method1(int a) {
        a++;
        System.out.println(a);
    }

    public static void method1(int[] a) {
        a[0]++;
    }

    public static void reverse(int[] a) {
        for (int i = 0; i < a.length / 2; i++) {
            // swap a[i] with a[a.length - 1 - i]
            int tmp = a[i];
            a[i] = a[a.length - 1 - i];
            a[a.length - 1 - i] = tmp;
        }
    }
}
