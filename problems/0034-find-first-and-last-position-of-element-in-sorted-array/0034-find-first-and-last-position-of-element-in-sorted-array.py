class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        start = 0
        end = len(nums)
        m = (start + end) // 2
        while start < end and m > - 1 and m < len(nums):
            if target == nums[m] and m - 1 <= -1 or target == nums[m] and m - 1 > - 1 and nums[m - 1] < nums[m]:
                ans[0] = m
                break
            elif target < nums[m] or target == nums[m] and m - 1 > - 1 and nums[m - 1] == target:
                end = m
            elif target > nums[m]:
                start = m + 1
            m = (start + end) // 2

        start = 0
        end = len(nums)
        m = (start + end) // 2
        while start < end and m > - 1 and m < len(nums):
            if target == nums[m] and m + 1 >= len(nums) or target == nums[m] and m + 1 < len(nums) and nums[m + 1] > nums[m]:
                ans[1] = m
                break
            elif target > nums[m] or target == nums[m] and m + 1 < len(nums) and nums[m + 1] == target:
                start = m + 1
            elif target < nums[m]:
                end = m
            m = (start + end) // 2
        
        return ans
        


            
        # O(log n) - time
        # O(1) - memory