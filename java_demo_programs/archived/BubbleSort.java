package archived;

public class BubbleSort {
    public static void main(String[] args) {
        int[] test = { 5, 3, 2, 1, 4, 6 };
        int[] result = bubbleSort1(test);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + " ");
        }
    }

    public static int[] bubbleSort1(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            // from left to right, compare two values and swap if needed
            for (int j = 0; j < array.length - 2; j++) {
                if (array[j] > array[j + 1]) {
                    swap(array, j, j + 1);
                }
            }
        }

        return array;
    }

    public static int[] bubbleSort2(int[] array) {
        boolean swapped = false;
        for (int i = 0; i < array.length - 1; i++) {
            swapped = false;
            // from left to right, compare two values and swap if needed
            for (int j = 0; j < array.length - 2; j++) {
                if (array[j] > array[j + 1]) {
                    swap(array, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                return array;
            }
        }

        return array;
    }

    public static void swap(int[] array, int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}
