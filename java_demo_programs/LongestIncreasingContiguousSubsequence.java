
public class LongestIncreasingContiguousSubsequence {

	public static void main(String[] args) {

		// int[] arr = { 3, 6, 5, 1, 9, 3, 2, 3, 4, 5, 1 };
		// longestForward(arr);
		// longestBackwards(arr);

		for (int i = 0; i < 10; i++) {
			if (i == 5) {
				continue;
			}
			System.out.println(i);
		}

	}

	public static void longestForward(int[] arr) {
		int sublength;
		int sublengthMax = 0;
		// int index = 0;
		int indexMax = 0;
		for (int i = 0; i < arr.length; i++) {
			sublength = 1;
			for (int j = i + 1; j < arr.length; j++) {
				if (arr[j - 1] < arr[j]) {
					sublength++;
					// index = j + 2 - sublength;
				} else {
					break;
				}
				if (sublength > sublengthMax) {
					sublengthMax = sublength;
					indexMax = i;
				}
			}
		}
		System.out.println(sublengthMax);
		for (int i = indexMax; i < sublengthMax + indexMax; i++) {
			System.out.print(arr[i] + " ");
		}
	}

	// public static void longestBackwards(int[] arr) {
	// int sublength;
	// int sublengthmax = 0;
	// int index = 0;
	// int indexmax = 0;
	// for (int i = arr.length - 1; i >= 0; i--) {
	// sublength = 1;
	// for(int j = i; j >= 1; j--) {
	// if(arr[j] < arr[j - 1]) {
	// sublength = sublength++;
	// index = j - 1;
	// }
	// if(sublength > sublengthmax) {
	// sublengthmax = sublength;
	// indexmax = index;
	// }
	// }
	// }
	// System.out.println(sublengthmax);
	// for (int i = indexmax; i < sublengthmax + indexmax - 1; i++) {
	// System.out.println(arr[i] + " ");
	// }
	// System.out.println();
	// }

}
