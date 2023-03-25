// Implement Queue using Array
public class QueueExample {
    public static int id;
    private int[] data;
    private int index; // index of the front element
    private int size = 0; // current number of elements

    public QueueExample(int capacity) {
        data = new int[capacity];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void enqueue(int value) {
        if (size == data.length) {
            return;
        }
        int position = (index + size) % data.length;
        data[position] = value;
        size++;
    }

    public int dequeue() {
        // implementation
        if (isEmpty()) {
            return Integer.MIN_VALUE;
        }

        int value = data[index];
        index = (index + 1) % data.length;
        size--;
        return value;
    }

    // return the first value in the queue, but doesn't remove
    public int first() throws Exception {
        if (isEmpty()) {
            throw new Exception();
        }

        return data[index];
    }
}
