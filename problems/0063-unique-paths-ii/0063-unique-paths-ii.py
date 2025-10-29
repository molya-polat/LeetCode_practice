class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    if obstacleGrid[m - 1][n - 1] == 1:
                        return 0
                    else:
                        dp[m - 1][n - 1] = 1
                else:
                    if obstacleGrid[i][j] != 1:
                        if i == m - 1:
                            dp[i][j] = dp[i][j+1]
                        elif j == n - 1:
                            dp[i][j] = dp[i + 1][j]
                        else:
                            dp[i][j] = dp[i + 1][j] + dp[i][j+1]
        return dp[0][0]
        # O(m*n) - time
        # O(m*n) - space