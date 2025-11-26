class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        m = (start + end) // 2
        while start < end and m > - 1 and m < len(nums):
            leftSide = True
            rightSide = True
            if m - 1 > -1 and nums[m - 1] >= nums[m]:
                leftSide = False
            if m + 1 < len(nums) and nums[m + 1] >= nums[m]:
                rightSide = False
            if leftSide and rightSide:
                return m
            if not leftSide:
                end = m
            else:
                start = m + 1
            m = (start + end) // 2
        
        return -1
        # O(n) - time
        # O(1) - memory