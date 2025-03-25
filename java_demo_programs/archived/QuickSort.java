package archived;

import java.util.Arrays;

public class QuickSort {

    public static void main(String[] args) {
        int[] test = new int[] { 4, 1, 2, 7, 5, -1, 8, 0, 6 };
        quickSort(test, 0, test.length - 1);
        System.out.println(Arrays.toString(test));
    }

    public static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pivot = partition(array, low, high);
            // System.out.println(pivot);
            // System.out.println(Arrays.toString(array));
            quickSort(array, low, pivot - 1);
            quickSort(array, pivot + 1, high);
        }
    }

    public static int partition(int[] array, int low, int high) {
        int pivot = array[low];
        int i = low + 1;

        for (int j = low; j <= high; j++) {
            if (array[j] < pivot) {
                swap(array, j, i);
                i++;
            }
        }

        swap(array, low, i - 1);
        return i - 1;
    }

    public static void swap(int[] array, int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}
