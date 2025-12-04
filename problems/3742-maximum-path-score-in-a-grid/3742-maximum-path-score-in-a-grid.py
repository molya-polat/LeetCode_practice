class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])


        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        score_add = {0: 0, 1: 1, 2: 2}
        cost_add = {0: 0, 1: 1, 2: 1}


        for i in range(m):
            for j in range(n):
                for cost_used in range(k + 1):
                    if dp[i][j][cost_used] == -1:
                        continue

                    cur_score = dp[i][j][cost_used]

                    if i + 1 < m:
                        nc = cost_used + cost_add[grid[i + 1][j]]
                        if nc <= k:
                            ns = cur_score + score_add[grid[i + 1][j]]
                            dp[i + 1][j][nc] = max(dp[i + 1][j][nc], ns)

                    if j + 1 < n:
                        nc = cost_used + cost_add[grid[i][j + 1]] 
                        if nc <= k:
                            ns = cur_score + score_add[grid[i][j + 1]]
                            dp[i][j + 1][nc] = max(dp[i][j + 1][nc], ns)



                          
        return max(dp[m-1][n-1])