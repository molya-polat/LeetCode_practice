class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        counter = 0
        start = 0
        while start + 2 < len(nums):
            if (nums[start] + nums[start + 2]) * 2 == nums[start + 1]:
                counter += 1
            start += 1
        
        return counter
        # O(n) - time compl
        # O(1) - space compl