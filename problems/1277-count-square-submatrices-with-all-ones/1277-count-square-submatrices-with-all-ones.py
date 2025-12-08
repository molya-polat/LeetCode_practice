class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        longest_ones_down = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            if i == m - 1:
                for j in range(n):
                    longest_ones_down[i][j] = matrix[i][j]
                continue

            for j in range(n):
                if matrix[i][j] == 1:
                    longest_ones_down[i][j] = 1 + longest_ones_down[i + 1][j]
                else:
                    longest_ones_down[i][j] = 0

        for i in range(m):
            for j in range(n):
                prev_ans = ans
                if longest_ones_down[i][j] > 0:
                    mn_side = longest_ones_down[i][j]
                    k = 0
                    while mn_side > k and j + k < n:
                        k += 1

                        if j + k < n:
                            mn_side = min(mn_side, longest_ones_down[i][j + k])
                    
                    ans += k

        return ans
                
# O(n^3) - time
#O(m * n) - memory