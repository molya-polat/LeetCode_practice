class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = -1
        if nums[0] > nums[len(nums) - 1]:
            start = 0
            end = len(nums)
            medium = (start + end) // 2 
            while medium > -1 and medium < len(nums):
                if end - start <= 2:
                    k = medium
                    break
                else:
                    if nums[medium] > nums[start]:
                        start = medium
                    elif nums[medium] <= nums[start]:
                        end = medium
                medium = (start + end) // 2
            if k + 1 < len(nums) and nums[k] > nums[k + 1]:
                k = k + 1
        start = 0
        end = len(nums)
        if k != -1:
            if target == nums[k]:
                return k
            elif target > nums[k] and target >= nums[start]:
                end = k
            elif target >= nums[k] and target <= nums[end - 1]:
                start = k
        medium = (start + end) // 2  
        while medium > -1 and medium < len(nums) and start < end:
            if target == nums[medium]:
                return medium
            if target < nums[medium]:
                end = medium
            elif target > nums[medium]:
                start = medium + 1
            medium = (start + end) // 2
        
        return -1
# O(log n) - time
# O(1) - memory