class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
        return sorted(nums)
        # time complexity O(n*logn)
        # space complexity O(n)