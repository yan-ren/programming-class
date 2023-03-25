import java.util.Scanner;

public class J5_2021 {
    public static void main(String[] args) {
        int m, n, k;
        int[] rows;
        int[] columns;

        Scanner sc = new Scanner(System.in);
        m = sc.nextInt();
        n = sc.nextInt();
        k = sc.nextInt();
        rows = new int[m];
        columns = new int[n];

        // 0 == Black, 1 == Gold
        for (int i = 0; i < k; i++) {
            String choice = sc.next();
            int index = sc.nextInt() - 1;
            if (choice.equals("R")) {
                rows[index] = rows[index] ^ 1;
            } else {
                columns[index] = columns[index] ^ 1;
            }
        }

        // count
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                count += rows[i] ^ columns[i];
            }
        }

        System.out.println(count);
    }
}