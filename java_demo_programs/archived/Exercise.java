package archived;

import java.util.Scanner;

public class Exercise {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();
    }

    public static boolean isSorted(int[] src) {
        for(int i = 0; i < src.length - 1; i++) {
            if (src[i] > src[i+1]) {
                return false;
            }
        }

        return true;
    }

    public static boolean isPalindrome(String src) {
        for(int i = 0; i < src.length()/2; i++) {
            if (src.charAt(i) != src.charAt(src.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }

    public static boolean isPrime(int value) {
        if(value <= 1) {
            return false;
        }

        for(int i = 2; i < value; i++) {
            if (value % i == 0) {
                return false;
            }
        }

        return true;
    }


}