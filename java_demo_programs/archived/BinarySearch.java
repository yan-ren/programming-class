package archived;

public class BinarySearch {
    public static void main(String[] args) {
        int[] canadidates = { 3, 4, 6, 7, 9, 12, 25 };
        int target = 3;

        System.out.println(search(canadidates, target));
    }

    public static boolean search(int[] candidates, int target) {

        int left = 0;
        int right = candidates.length - 1;

        while (left <= right) {
            int mid = (right + left) / 2;

            if (candidates[mid] < target) {
                left = mid + 1;
            } else if (candidates[mid] > target) {
                right = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
}
