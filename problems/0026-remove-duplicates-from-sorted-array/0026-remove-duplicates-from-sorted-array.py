class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1] and front < len(nums):
                while front < len(nums) and nums[front] <= nums[i - 1]:
                    front += 1
                if front >= len(nums):
                    nums[i] = 0
                else:
                    nums[i] = nums[front]
                    length += 1
            elif front >= len(nums):
                nums[i] = 0
            else:
                length += 1
        return length

        # O(n) - time
        # O(1) - space