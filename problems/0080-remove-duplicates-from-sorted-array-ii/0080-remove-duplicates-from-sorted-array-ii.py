class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        front = 1
        twice = False
        for i in range(1, len(nums)):
            if front >= len(nums):
                nums[i] = 0
            else:
                if twice:
                    while front < len(nums) and nums[i - 1] >= nums[front]:
                        front += 1
                    if front < len(nums):
                        nums[i] = nums[front]
                        length += 1
                        front += 1
                        twice = False
                    else:
                        nums[i] = 0
                else:
                    nums[i] = nums[front]
                    front += 1
                    if nums[i] == nums[i - 1]:
                        twice = True
                    length += 1

        return length
    # O(n) - time
    # O(1) - space