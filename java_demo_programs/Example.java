
public class Example {
    public static void main(String[] args) {
        /*
         * given a 2-d array e.g. { {1, 2, 3}, {3, 4}, {5, 6, 7, 8} } sum each subarray
         * to a single value, build the sum into a single array {6, 7, 26}
         */
        // int[][] input = { { 1, 2, 3 }, { 3, 4 }, { 5, 6, 7, 8 } };
        // int[] result = new int[input.length];
        // for (int level = 0; level < input.length; level++) {
        // int sum = 0;
        // for (int i = 0; i < input[level].length; i++) {
        // sum += input[level][i];
        // }
        // result[level] = sum;
        // }

        // for (int i = 0; i < result.length; i++) {
        // System.out.println(result[i]);
        // }

        // int[] a = { 1, 2, 3, 4 };
        // int largest = a[0];
        // int secondLargest = a[1];
        // for (int i = 0; i < a.length; i++) {
        // if (a[i] > largest) {
        // secondLargest = largest;
        // largest = a[i];
        // } else if (a[i] > secondLargest) {
        // secondLargest = a[i];
        // }
        // }
        // System.out.println(secondLargest);

        // int c = power(2, 3);
        // System.out.println(c);

        // System.out.println(power(2, 4));
        // int[] a = { 1, 2, 3, 4, 5, 6 };
        // skipPrint(a, 2);

        // method overloading: multiple method can have the same name with different
        // parameters(inputs)
        // method1();

        int[] x = { 1 };
        increment(x);
        System.out.println(x[0]);
    }

    public static boolean arrEqual(int[] arr1, int[] arr2) {
        boolean equal = true;
        if (arr1.length == arr2.length) {
            for (int i = 0; i < arr1.length; i++) {
                if (arr1[i] != arr2[i]) {
                    equal = false;
                }
            }
        } else {
            equal = false;
        }
        return equal;
    }

    public static void increment(int[] a) {
        a[0]++;
        System.out.println(a[0]);
    }

    public static int method1(int a, int b) {
        System.out.println(a);
        return 0;
    }

    public static void method1(int b, String s) {
        System.out.println("method1");
    }

    // a^b: a is integer, b is integer, a^b is integer as well
    public static int power(int a, int b) {
        int result = 1;
        for (int i = 0; i < b; i++) {
            result = result * a;
        }
        return result;
    }

    public static void skipPrint(int[] arr, int n) {
        for (int i = n; i < arr.length; i += n) {
            System.out.println(arr[i]);
        }
    }

    /*
     * given an integer array {1, 2, 3, 4, 5, 6} split the integer into two integer
     * arrays where one array contains all even numbers and another array contains
     * all odd numbers
     */

    /*
     * remove array duplicates given an integer array, write a function that returns
     * a new array with duplicated value removed
     * 
     * {1, 2, 2, 3, 4, 5, 5} {1, 2, 3, 4, 5}
     * 
     */

}