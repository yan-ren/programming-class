public class OtherSimpleSorting {
    public static void main(String[] args) {
        int[] test = { 5, 3, 2, 1, 4, 6 };
        insertionSort(test);

        for (int i = 0; i < test.length; i++) {
            System.out.println(test[i]);
        }
    }

    public static void selectionSort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int lowest = i;
            for (int j = i; j < a.length; j++) {
                if (a[j] < a[lowest]) {
                    lowest = j;
                }
            }

            swap(a, i, lowest);
        }
    }

    public static void insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int target = a[i];
            int targetIndex = i;
            int j = i - 1;
            while (j >= 0 && a[j] > target) {
                swap(a, targetIndex, j);
                targetIndex = j;
                j--;
            }
        }
    }

    public static void swap(int[] array, int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}
