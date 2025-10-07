class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        altSum = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                altSum += num
            else:
                altSum -= num
        return altSum

        # O(n) - time complexity
        # O(1) - space complexity