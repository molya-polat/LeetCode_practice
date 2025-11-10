class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        dp = [0 for _ in range(len(groups))]
        dp[len(groups) - 1] = 1
        for i in range(len(groups) - 2, -1, -1):
            if groups[i] != groups[i + 1]:
                dp[i] = 1 + dp[i + 1]
            else:
                dp[i] = dp[i + 1]

        maxDp = max(dp)
        maxDpIndex = dp.index(maxDp)
        ans.append(words[maxDpIndex])
        for i in range(maxDpIndex + 1, len(groups)):
            if groups[i - 1] != groups[i]:
                ans.append(words[i])
        return ans
        # O(len(groups)) - time
        # O(len(groups)) - memory