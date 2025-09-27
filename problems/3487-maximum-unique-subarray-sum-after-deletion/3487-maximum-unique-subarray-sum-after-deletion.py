class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxSum = 0
        dictionary = {}
        hasPositiveNum = False
        for num in nums:
            if num not in dictionary and num > 0:
                hasPositiveNum = True
                dictionary[num] = 1
                maxSum += num
            elif num in dictionary:
                dictionary[num] += 1
        return maxSum if hasPositiveNum else max(nums)