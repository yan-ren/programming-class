package class0303;

import java.util.Scanner;

public class Class4 {
    public static void main(String[] args) {
        int number = 10;
        double decimal = 10.1;

        // Reference Type
//        String s = "hello";
//        String t = "world";
//        String word = s + t;
//        System.out.println(word);
//
//        Scanner sc = new Scanner(System.in);
//        String name = sc.nextLine();
//        if (name.equals("Tom")) {
//            System.out.println("Welcome " + name);
//        } else
//        {
//            System.out.println("Login failed");
//        }
//        int a = 2;
//        int b = 1;
//
//        System.out.println(a == b);

//        Scanner sc = new Scanner(System.in);
//        String someString = "abc";
//        String otherString = sc.nextLine();
//        System.out.println(someString.equals(otherString));
//        System.out.println(someString.length());
//        System.out.println(someString.charAt(0));

        Scanner sc = new Scanner(System.in);
        System.out.println("Create a password:");
        String password = sc.nextLine();
        if (password.length() < 8) {
            System.out.println("Invalid");
        } else {
            System.out.println("Password created");
        }
    }
}
