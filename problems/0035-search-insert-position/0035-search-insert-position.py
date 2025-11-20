class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        m = (start + end) // 2
        while m > - 1 and m < len(nums) and start < end:
            if target == nums[m]:
                return m
            elif target < nums[m]:
                end = m
            else:
                start = m + 1
            m = (start + end) // 2
        
        return m
        # O(logn) - time
        # O(1) - memory