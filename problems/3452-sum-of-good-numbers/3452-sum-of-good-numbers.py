class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        goodSum = 0
        length = len(nums)
        for i, num in enumerate(nums):
            if (i - k < 0 or nums[i - k] < num) and (i + k >= length or nums[i + k] < num):
                goodSum += num
        return goodSum

        # O(n) - time compl
        # O(1) - space compl