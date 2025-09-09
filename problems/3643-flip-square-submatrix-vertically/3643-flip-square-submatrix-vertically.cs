public class Solution {
    public int[][] ReverseSubmatrix(int[][] grid, int x, int y, int k) {
        int[][] reversedMatrix = new int [grid.Length][];
        for (int s = 0; s < reversedMatrix.Length; s++){
            reversedMatrix[s] = new int [grid[0].Length];
        }
        int m = grid.Length;
        int n = grid[0].Length;
        for(int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if((i < x || i >= x + k) || (j < y || j >= y + k)){
                    reversedMatrix[i][j] = grid[i][j];
                }
                else {
                    reversedMatrix[i][j] = grid[2 * x + k - 1 - i][j];
                }

                
            }
        }
        return reversedMatrix;
       
    }
}