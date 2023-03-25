import java.util.HashSet;
import java.util.Stack;

import javax.print.attribute.HashPrintJobAttributeSet;

import java.util.*;

public class BalanceBracket {
    public static void main(String[] args) {
        // Quadrilateral a = new Quadrilateral();
        // String expression = "[()]{}{[()()]()}";
        // System.out.println(isBalanced(expression));

        // System.out.println(isBalanced("[(]"));

        // String equation = "2*(2+3)/4+5";

        // Set<String> set1 = new HashSet<>();
        // HashSet<String> set2 = new HashSet<>();
        // set1.add("a");
        // set1.add("b");
        // set1.add("c");

        // set2.add("b");
        // set2.add("c");
        // set2.add("d");

        // set1.removeAll(set2);
        // System.out.println(set1);
        // System.out.println(set2);

        // key: String, value: String
        // HashMap<String, String> map = new HashMap<>();
        // map.put("a", "first");
        // map.put("b", "second");
        // if(map.containsKey("a")) {

        // }

        // if(map.containsValue("first")) {

        // }

        // for(String key: map.keySet()) {
        // System.out.println(key);
        // System.out.println(map.get(key));
        // }

        // for(Map.Entry<String, String> entry: map.entrySet()){
        // System.out.println(entry.getKey());
        // System.out.println(entry.getValue());
        // }

        // given a string of letters find out which letter showed up the most
        // "abbbc" -> {"a": 2, "b": 2, "c": 1}
        String text = "aabbc";
        text.equals("aabbc");
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < text.length(); i++) {
            if (map.containsKey(text.charAt(i))) {
                map.put(text.charAt(i), map.get(text.charAt(i)) + 1);
            } else {
                map.put(text.charAt(i), 1);
            }
        }

        // find the key with largest value
        int largestValue = -1;
        char mostKey = ' ';
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            if (entry.getValue() > largestValue) {
                largestValue = entry.getValue();
                mostKey = entry.getKey();
            }
        }
        System.out.println(mostKey);
    }

    public static boolean isBalanced(String expression) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '{' || expression.charAt(i) == '(' || expression.charAt(i) == '[') {
                stack.push(expression.charAt(i));
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char valueInStack = stack.pop();
                // System.out.println(valueInStack);
                if (!inPair(valueInStack, expression.charAt(i))) {
                    return false;
                }
            }
            // System.out.println(stack);
        }

        return stack.isEmpty();
    }

    public static boolean inPair(char c1, char c2) {
        if ((c1 == '{' && c2 == '}') || (c1 == '(' && c2 == ')') || (c1 == '[' && c2 == ']')) {
            return true;
        }

        return false;
    }

    private int[] testArray = { 3, 4, 5 };

    /** @param n an int to be incremented by 1 */
    public void increment(int[] arr, int index) {
        arr[index]++;
    }

    public void firstTestMethod() {
        for (int i = 0; i < testArray.length; i++) {
            increment(testArray, i);
            System.out.print(testArray[i] + " ");
        }
    }
}

abstract class Quadrilateral {

}
