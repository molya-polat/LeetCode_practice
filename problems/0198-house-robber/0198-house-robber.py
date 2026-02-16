class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        length = len(nums)
        if length < 3:
            return max(nums)                
        dp[length - 1] = nums[length - 1]
        dp[length - 2] = nums[length - 2]
        dp[length - 3] = nums[length - 1] + nums[length - 3]

        for i in range(length - 4, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
        

        return max(dp[0], dp[1])

# O(n) - time
# O(n) - space