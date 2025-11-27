class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1] or len(nums) < 2:
            return nums[0]
        else:
            start = 0 
            end = len(nums)
            m = (start + end) // 2
            while start < end and m > -1 and m < len(nums):
                if m - 1 > - 1 and nums[m - 1] > nums[m]:
                    return nums[m]
                elif nums[m] >= nums[0] and nums[m] >= nums[len(nums) - 1]:
                    start = m + 1
                elif nums[m] <= nums[0] and nums[m] <= nums[len(nums) - 1]:
                    end = m
                m = (start + end) // 2
            
        
        return -1
        # O(logn) - time
        # O(1) - memory