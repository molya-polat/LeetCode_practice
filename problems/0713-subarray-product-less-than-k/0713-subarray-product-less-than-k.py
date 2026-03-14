class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, end = 0, -1
        multiply = 1
        ct = 0

        while start != len(nums):
            while end + 1 < len(nums) and (multiply * nums[end + 1]) < k:
                end += 1
                multiply = multiply * nums[end]

            ct += end - start + 1
            if start <= end:
                multiply = multiply // nums[start]
            else:
                end += 1
            start += 1
        
        return ct
        # O(n) - time
        # O(1) - space