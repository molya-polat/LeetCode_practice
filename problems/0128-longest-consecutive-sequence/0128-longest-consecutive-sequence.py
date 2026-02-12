class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()

        length = 1
        prev = nums[0]
        maxLength = 0
        for i,n in enumerate(nums):
            if i != 0:
                if n - prev == 1:
                    length += 1
                elif n - prev != 0 and n - prev != 1:
                    length = 1
            maxLength = max(maxLength, length)
            prev = n
        
        return maxLength

        # O(n logn) - time
        # O(n) - space