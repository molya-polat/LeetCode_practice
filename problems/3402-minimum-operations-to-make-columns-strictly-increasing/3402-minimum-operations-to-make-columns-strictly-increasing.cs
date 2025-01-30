public class Solution {
    public int MinimumOperations(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int ops = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m - 1; j++) {
                if(grid[j][i] >= grid[j + 1][i]) {
                    ops += (grid[j][i] + 1) - grid[j + 1][i];
                    grid[j + 1][i] = grid[j][i] + 1;
                }   
            }
        }
        return ops;

    }
}