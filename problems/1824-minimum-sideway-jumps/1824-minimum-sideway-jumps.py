class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        m = len(obstacles) 
        dp = [(0, 0, 0) for _ in range(m)]
        INF = 10**9
        dp[0] = (1, 0, 1)
        if obstacles[1] == 1:
            dp[0] = (INF, 0, 1)
        if obstacles[1] == 2:
            dp[0] = (1, INF, 1)
        if obstacles[1] == 3:
            dp[0] = (1, 0, INF)
        
        
        for i in range(1, m - 1):
            prev_lane1, prev_lane2, prev_lane3 = dp[i - 1]
            lane1 = min(prev_lane1, 1 + min(prev_lane2, prev_lane3))
            lane2 = min(prev_lane2, 1 + min(prev_lane1, prev_lane3))
            lane3 = min(prev_lane3, 1 + min(prev_lane2, prev_lane1))
            if obstacles[i + 1] == 1 or obstacles[i] == 1 :
                lane1 = INF
            if obstacles[i + 1] == 2 or obstacles[i] == 2:
                lane2 = INF
            if obstacles[i + 1] == 3 or obstacles[i] == 3 :
                lane3 = INF
            dp[i] = (lane1, lane2, lane3)

        result_lane1, result_lane2, result_lane3 = dp[m - 2]
        return min(result_lane1, result_lane2, result_lane3)

        # O(m) - time
        # O(m) - space