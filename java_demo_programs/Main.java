import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] P = new int[N];
        int[] W = new int[N];
        int[] D = new int[N];

        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
            W[i] = sc.nextInt();
            D[i] = sc.nextInt();
        }

        int l = Integer.MIN_VALUE;
        int r = Integer.MAX_VALUE;

        // binary search
        while (l < r) {
            int c = (l + r + 1) / 2;
            if (minTime(c, P, D, W) <= minTime(c - 1, P, D, W)) {
                l = c;
            } else {
                r = c - 1;
            }
        }

        System.out.println(minTime(l, P, D, W));
    }

    public static long minTime(int c, int[] P, int[] D, int[] W) {
        long time = 0;
        for (int i = 0; i < P.length; i++) {
            long dist = Math.abs(c - P[i]);
            if (dist > D[i]) {
                time += (int) W[i] * (dist - D[i]);
            }
        }
        return time;
    }
}
