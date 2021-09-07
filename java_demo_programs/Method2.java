
import java.util.Scanner;

public class Method2 {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4 };
        printArray(arr);
    }

    public static void askToAddAndPrint(int[] arr, Scanner sc) {
        int index = sc.nextInt();
        int value = sc.nextInt();
        if (index >= arr.length) {
            System.out.println("invalid index");
            return;
        }
        arr[index] = value;
        printArray(arr);
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
