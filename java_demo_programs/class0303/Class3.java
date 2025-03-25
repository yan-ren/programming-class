package class0303;

public class Class3 {
    public static void main(String[] args) {
//        int x; // integer
//        x = 10;
//        System.out.println(x + 10);

        // primitive data type
        /*
        byte: -128 ~ 127
        short: -2^15 ~ 2^15-1
        int: -2^31 ~ 2^31 - 1
        long: -2^63 ~ 2^63 - 1

        float:
        double:

        boolean
        char
         */
//        byte value = 128;
//        int y = 1000;
//        double z = 1.123;
//        boolean x = true;
//        boolean y = false;
//
//        char c = '#';

        // equal sign in programming means assign right value to the left
//        int x = 10;
//        int y = 20;
//        int z = x + y;
//
//        x = x + 2;
//
//        System.out.println(z);
//        System.out.println(x);

//        double x = 1;
//        double y = 1.3;
//        int z = 3;
//        System.out.println(x);

        // + - * /
//        int x = 2;
//        double y = 3.0;
//        double z = x + y;
//        System.out.println(x + y);
    /*
    1. How many seconds are there in 42 minutes 42 seconds?
    2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in 1 mile.
    3. If you run a 10 kilometers race in 42 minutes 42 seconds, what is your average speed (time per
mile in seconds)? What is your average speed in miles per hour?
     */

        int minutes = 42;
        int seconds = 42;
        int totalSeconds = minutes * 60 + seconds;
        System.out.println(totalSeconds);
    }
}
