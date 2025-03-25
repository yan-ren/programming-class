package archived;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class CollectionExample {
    public static void main(String[] args) {
        // String[] arr = new String[4];
        // arr[0] = "tom";
        // arr[1] = "jerry";
        // System.out.println(arr[0]);

        // ArrayList<String> names = new ArrayList<>();
        // names.add("tom");
        // names.add("jerry");
        // System.out.println(names.get(0));
        // System.out.println(names);
        // System.out.println(names.size());
        // names.add("kim");
        // System.out.println(names.size());
        // names.remove(0);
        // System.out.println(names);
        // names.set(0, "tommy");

        // for (int i = 0; i < names.size(); i++) {
        //     System.out.println(names.get(i));
        // }

        // // for each loop
        // for(String s: names) {
        //     s = "abc";
        //     System.out.println(s);
        // }

        // ArrayList<Integer> numbers = new ArrayList<>();
        // numbers.add(1);

        // Collections.sort(numbers);
        Stack<String> cards = new Stack<>();
        cards.push("one");
        cards.push("two");
        
        System.out.println(cards);

        System.out.println(cards.pop());
    }

    public static int[] sortUglyNumbers(int arr[]) {
        ArrayList<Integer> uglyNumbers = new ArrayList<>();

        for(int i = 0; i < arr.length; i++){
            if(isUgly(arr[i])){
                uglyNumbers.add(arr[i]);
                arr[i] = -1;
            }
        }

        Collections.sort(uglyNumbers);

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == -1) {
                arr[i] = uglyNumbers.get(0);
                uglyNumbers.remove(0);
            }
        }

        return arr;
    }

    public static boolean isUgly(int n){
        while(n % 2 == 0) {
            n = n / 2;
        }

        while(n % 3 == 0) {
            n = n / 3;
        }

        while(n % 5 == 0) {
            n = n / 5;
        }

        if (n == 1) {
            return true;
        }

        return false;
    }
}
