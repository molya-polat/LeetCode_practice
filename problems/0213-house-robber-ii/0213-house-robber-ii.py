class Solution:
    def rob1(self, nums: List[int]) -> int:
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


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)  

        possible1 = nums[n - 1] + self.rob1(nums[1 : n - 2])
        possible2 = self.rob1(nums[0 : n - 1])

        return max(possible1, possible2)