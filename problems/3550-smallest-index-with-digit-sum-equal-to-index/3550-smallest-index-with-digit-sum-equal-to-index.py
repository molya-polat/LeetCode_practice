class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number = nums[i]
            sm = 0
            while number > 0:
                sm += number % 10
                number = number // 10
            if sm == i:
                return i
        return -1