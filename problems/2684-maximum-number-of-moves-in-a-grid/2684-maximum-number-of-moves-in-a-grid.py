class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])
        mxAns = 0
        def maxMovesFrom(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                if j == n - 1:
                    memo[(i, j)] = 0
                    return 0
                a, b, c = 0, 0, 0
                if i != 0:
                    if grid[i][j] < grid[i - 1][j + 1]:
                        a = 1 + maxMovesFrom(i - 1, j + 1)
                if grid[i][j] < grid[i][j + 1]:
                    b = 1 + maxMovesFrom(i, j + 1)
                if i != m - 1:
                    if grid[i][j] < grid[i + 1][j + 1]:
                        c = 1 + maxMovesFrom(i + 1, j + 1)
                mx = max(a,b,c)
                memo[(i, j)] = mx
                return mx

        for i in range(m):
            mxAns = max(mxAns, maxMovesFrom(i, 0))
            if mxAns == n - 1:
                break
        return mxAns
        # O(m*n) - memory
        # O(m*n) - time