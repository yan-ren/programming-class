import java.util.Arrays;

public class ArrayStack {
    private int capacity = 0;
    private int[] data;
    private int top = 0;

    public ArrayStack(int capacity) {
        this.capacity = capacity;
        data = new int[capacity];
    }

    public void push(int value) {
        if (top == data.length) {
            System.err.println("stack is full");
        }

        data[top] = value;
        top++;
    }

    public int pop() {
        if (top == 0) {
            System.err.println("stack is empty");
        }

        int output = data[top - 1];
        top--;
        return output;
    }

    public int size() {
        return top;
    }

    public String toString() {
        return Arrays.toString(data);
    }
}

/*
 * If a language doesn't have array,
 * you can build a list/array like data structure first and use the list to
 * create stack
 * 
 * Java genetic
 */