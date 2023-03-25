import java.util.LinkedList;
import java.util.Queue;

public class NumberOfIslands {
    /*
     * grid = [
     * [1, 1, 0, 0, 0],
     * [1, 1, 0, 0, 0],
     * [0, 0, 1, 0, 0],
     * [0, 0, 0, 1, 1]
     * ]
     */
    public static void main(String[] args) {
        int[][] grid = {
                { 1, 1, 0, 0, 0 },
                { 1, 1, 0, 0, 0 },
                { 0, 0, 1, 0, 0 },
                { 0, 0, 0, 1, 1 }
        };
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    findIsland(grid, i, j);
                    count += 1;
                }
            }

        }

        System.out.println(count);
    }

    // visit all neighbors of (i, j)
    public static void findIsland(int[][] grid, int i, int j) {
        // [i, j]
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] { i, j });
        // whenever visit 1, change to 0 to avoid visit it again
        grid[i][j] = 0;

        while (!queue.isEmpty()) {
            int[] point = queue.poll();

            // for current point, check four directions
            // top
            int x = point[0];
            int y = point[1] - 1;
            if (isValid(grid, x, y) && grid[x][y] == 1) {
                queue.add(new int[] { x, y });
                grid[x][y] = 0;
            }

            // right
            x = point[0] + 1;
            y = point[1];
            if (isValid(grid, x, y) && grid[x][y] == 1) {
                queue.add(new int[] { x, y });
                grid[x][y] = 0;
            }
            // bottom
            x = point[0];
            y = point[1] + 1;
            if (isValid(grid, x, y) && grid[x][y] == 1) {
                queue.add(new int[] { x, y });
                grid[x][y] = 0;
            }
            // left
            x = point[0] - 1;
            y = point[1];
            if (isValid(grid, x, y) && grid[x][y] == 1) {
                queue.add(new int[] { x, y });
                grid[x][y] = 0;
            }
        }
    }

    public static boolean isValid(int[][] grid, int x, int y) {
        return x >= 0 && x < grid.length && y >= 0 && y < grid[0].length;
    }
}
