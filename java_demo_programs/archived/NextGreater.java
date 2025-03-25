package archived;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class NextGreater {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(getNextGreater(new int[] { 3, 2, 8, 7, 9, 17, 12 })));
    }

    public static int[] getNextGreater(int[] numbers) {
        List<Integer> output = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(numbers[0]);

        for (int i = 1; i < numbers.length; i++) {
            while (!stack.isEmpty() && stack.peek() < numbers[i]) {
                stack.pop();
                output.add(numbers[i]);
            }
            stack.push(numbers[i]);
        }

        while (!stack.isEmpty()) {
            output.add(-1);
            stack.pop();
        }

        return output.stream().mapToInt(i -> i).toArray();
    }
}