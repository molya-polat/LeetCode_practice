class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        memo = {}

        def rec_dp(i, j):
            if i < 0 or j < 0:
                return max(i, j) + 1
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                ans = rec_dp(i - 1, j - 1)
            else:
                ans1 = 1 + rec_dp(i - 1, j - 1)
                ans2 = 1 + rec_dp(i, j - 1)
                ans3 = 1 + rec_dp(i - 1, j)
                ans = min(ans1, ans2, ans3)

            memo[(i, j)] = ans
            return ans


        
        return rec_dp(n - 1, m - 1)