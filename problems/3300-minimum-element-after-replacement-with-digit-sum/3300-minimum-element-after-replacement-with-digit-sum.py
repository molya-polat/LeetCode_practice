class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            sm = 0
            while n > 0:
                sm += n % 10
                n = n // 10

            nums[i] = sm
        return min(nums)
        # O(nlogn) - time
        # O(1) - space