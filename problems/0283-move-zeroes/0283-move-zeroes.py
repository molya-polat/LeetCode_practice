class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                end = i + 1
                while end < len(nums) and nums[end] == 0:
                    end += 1
                if end < len(nums):
                    temp = nums[i]
                    nums[i] = nums[end]
                    nums[end] = temp