class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        INF = 1e9
        
        def find_min_sum(i, j, triangle):
            if i == n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = triangle[i][j] + min(find_min_sum(i + 1, j, triangle), find_min_sum(i + 1, j + 1, triangle))
            memo[(i, j)] = ans
            return ans

        return find_min_sum(0, 0, triangle)
        # O(n^2) - time
        # O(n^2) - memory
        
















        # dp = [(0, 0) for _ in range(n)] # min sum starting from i-th row
        # dp[0] = (triangle[0][0], 0)

        # def min_el(triangle_row, index):
        #     if triangle_row[index] <= triangle_row[index + 1]:
        #         return (triangle_row[index], index)
        #     else:
        #         return (triangle_row[index + 1], index + 1)

        # for i in range(1, n):
        #     triangle_row = triangle[i]
        #     index = dp[i-1][1]
        #     min_element_index = min_el(triangle_row, index)
        #     dp[i] = (dp[i - 1][0] + min_element_index[0], min_element_index[1])
        
        # return dp[n - 1][0]