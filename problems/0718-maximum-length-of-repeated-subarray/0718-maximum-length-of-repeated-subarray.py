class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if nums1[i] == nums2[j]:
	                dp[i][j] = 1 + dp[i + 1][j + 1]
        max_length = 0
        for i in range(l1):
            for j in range(l2):
                max_length = max(max_length, dp[i][j])
        return max_length