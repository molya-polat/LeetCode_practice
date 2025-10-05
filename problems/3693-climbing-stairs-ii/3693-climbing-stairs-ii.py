class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        INF = 10 ** 9
        costs = [0] + costs

        # costs[n]
        # costs[1] + (1 - 0) ^ 2
        # costs[2] + (2 - 0) ^ 2

        dp = [0 for _ in range(n + 1)]
        
        # dp will be - starting at step i, whats the minimal cost to reach n

        dp[n] = 0
        # dp[n - 1] = costs[n] + 1
        # dp[n - 2] = min(costs[n] + 4, costs[n - 1] + 1 + dp[n - 1])
        # dp[n - 3] = min(costs[n] + 9, costs[n - 1] + 4 + dp[n - 1], costs[n - 2] + 1 + dp[n - 2])
        # dp[n - 4] = min(costs[n - 1] + 9 + dp[n - 1], costs[n - 2] + 4 + dp[n - 2], costs[n - 3] + 1 + dp[n - 3])
        # dp[n - 5] = 

        for i in range(n - 1, -1, -1):
            
            first_path = costs[i + 3] + 9 + dp[i + 3] if i < n - 2 else INF
            second_path = costs[i + 2] + 4 + dp[i + 2] if i < n - 1 else INF
            third_path = costs[i + 1] + 1 + dp[i + 1]

            dp[i] = min(first_path, second_path, third_path)

        # Our answer then will be dp[0]
        return dp[0]

        # O(n) - time complexity
        # O(n) - space complexity