class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        column_prefix_sum = {}
        column_sums = []
        total_sm = 0
        for i in range(n):
            sm = 0
            for j in range(m):
                sm += grid[j][i]
            total_sm += sm
            column_prefix_sum[i] = total_sm
            column_sums.append((sm, i))
        
        current_sm = 0
        for i in range(len(column_sums) - 1, -1, -1):
            current_sm += column_sums[i][0]
            column = column_sums[i][1]
            if column > 0 and column_prefix_sum[column - 1] == current_sm:
                return True
        

        row_prefix_sum = {}
        row_sums = []
        total_sm = 0
        for i in range(m):
            sm = 0
            for j in range(n):
                sm += grid[i][j]
            total_sm += sm
            row_prefix_sum[i] = total_sm
            row_sums.append((sm, i))
        
        current_sm = 0
        for i in range(len(row_sums) - 1, -1, -1):
            current_sm += row_sums[i][0]
            row = row_sums[i][1]
            if row > 0 and row_prefix_sum[row - 1] == current_sm:
                return True
        
        return False

        # O(m * n) - time
        # O(m + n) - space