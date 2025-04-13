package class0303;

/*
Searching:

Find an item from a sequence of element

Sequential Search
Binary Search

Find element from a sorted array, sorted array [10, 20, 30, 40, 55]
 */
public class Class6 {
    public static void main(String[] args) {
        int[] numbers = {4, 3, 2, 1};
        for(int i: numbers) {
            System.out.println(i);
        }
        selectionSort(numbers);
        for(int i: numbers) {
            System.out.println(i);
        }
    }

    /*
        numbers = [1, 3, 2, 5, 4], target = 5
        return 4

        numbers = [1, 3, 2, 5, 4], target = 10
        return -1

        sequential search: starts from the first element and compare each element with target until the target is found
        or there are not more elements in the array
     */
    public static int search(int[] numbers, int target) {
        for(int i = 0; i < numbers.length; i++) {
            if(numbers[i] == target) {
                return i;
            }
        }

        return -1;
    }

    public static void selectionSort(int[] arr) {
        for(int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;

            for (int j = i+1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // swap
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int j = i;

            while (j > 0 && arr[j] < arr[j-1]) {
                int temp = arr[j];
                arr[j]=arr[j-1];
                arr[j-1] = temp;

                j--;
            }
        }
    }

    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

}
