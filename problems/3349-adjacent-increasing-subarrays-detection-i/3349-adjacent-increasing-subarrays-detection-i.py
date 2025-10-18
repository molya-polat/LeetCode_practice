class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_strictly_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True

        for i in range(len(nums) - 2 * k):
            first_arr = nums[i:i + k]
            second_arr = nums[i + k:i + 2 * k]

            if is_strictly_increasing(first_arr) and is_strictly_increasing(second_arr):
                return True
        
        return False