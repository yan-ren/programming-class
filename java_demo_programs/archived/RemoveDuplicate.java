package archived;

public class RemoveDuplicate {
    public static void main(String[] args) {
        int[] input = { 1, 2, 2, 3, 4, 5, 5 };
        int[] output = deduplicated(input);

        for (int i = 0; i < output.length; i++) {
            System.out.println(output[i]);
        }
    }

    public static int[] deduplicated(int[] arr) {
        int[] result = new int[arr.length];
        int resultIndex = 0;
        for (int i = 0; i < arr.length; i++) {
            // for each value in arr, check if already in result
            boolean exist = false;
            for (int j = 0; j < resultIndex; j++) {
                if (result[j] == arr[i]) {
                    exist = true;
                }
            }

            if (!exist) {
                result[resultIndex] = arr[i];
                resultIndex++;
            }
        }

        // resize result array, remove the unused position
        int[] newResult = new int[resultIndex];
        for (int i = 0; i < resultIndex; i++) {
            newResult[i] = result[i];
        }

        return newResult;
    }
}
