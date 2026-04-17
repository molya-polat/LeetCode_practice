class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        mindif = 10 ** 9
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == 1 and nums[j] == 2 or nums[i] == 2 and nums[j] == 1:
                    mindif = min(abs(i - j), mindif)
        
        if mindif > 10 ** 8:
            return -1
        return mindif
        # O(n^2) - time
        # O(1) - space