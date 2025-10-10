class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        zigzag = []
        startPosition = len(grid[0]) - 1 if len(grid[0]) % 2 == 0 else len(grid[0]) - 2
        for i, row in enumerate(grid):
            if i % 2 == 0:
                for j in range(0, len(grid[i]), 2):
                    zigzag.append(grid[i][j])
            else:
                for j in range(startPosition, -1, -2):
                    zigzag.append(grid[i][j])
        
        return zigzag

        # O(m*n) - time compl
        #  O(m*n) - space compl