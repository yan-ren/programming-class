import java.util.Arrays;

public class MergeSort {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(mergeSort(new int[] { 1, 4, 3, 2, 5 })));
    }

    public static int[] mergeSort(int[] a) {
        if (a.length == 1) {
            return a;
        }

        int[] a1 = Arrays.copyOfRange(a, 0, a.length / 2);
        int[] a2 = Arrays.copyOfRange(a, a.length / 2, a.length);

        a1 = mergeSort(a1);
        a2 = mergeSort(a2);

        return merge(a1, a2);
    }

    /*
     * a1 = [1, 2, 5]
     * a2 = [3, 4]
     * 
     * return [1, 2, 3, 4, 5]
     */
    public static int[] merge(int[] a1, int[] a2) {
        int[] res = new int[a1.length + a2.length];
        int index = 0;
        int i = 0;
        int j = 0;

        while (i < a1.length && j < a2.length) {
            if (a1[i] < a2[j]) {
                res[index] = a1[i];
                i++;
            } else {
                res[index] = a2[j];
                j++;
            }
            index++;
        }

        while (i < a1.length) {
            res[index] = a1[i];
            i++;
            index++;
        }

        while (j < a2.length) {
            res[index] = a2[j];
            j++;
            index++;
        }

        return res;
    }
}
