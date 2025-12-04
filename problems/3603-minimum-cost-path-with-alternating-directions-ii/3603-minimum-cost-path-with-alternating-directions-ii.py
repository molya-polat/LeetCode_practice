class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    dp[i][j] = (i + 1) * (j + 1) + waitCost[i][j] + dp[i][j - 1]
                elif j == 0 and i != 0:
                    dp[i][j] = (i + 1) * (j + 1) + waitCost[i][j] + dp[i - 1][j]
                elif i != 0 and j != 0:
                    dp[i][j] = (i + 1) * (j + 1) + waitCost[i][j] + min(dp[i - 1][j], dp[i][j - 1])

                if i == m - 1 and j == n - 1:
                    dp[i][j] -= waitCost[i][j]
                
        
        return dp[m - 1][n - 1]

        # O(m * n) - time
        # O(m * n) - memory