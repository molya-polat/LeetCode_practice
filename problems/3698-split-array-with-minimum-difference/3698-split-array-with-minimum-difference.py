class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        mx, ind_mx = -1, -1
        for i, k in enumerate(nums):
            if ind_mx == -1 or mx < k:
                ind_mx, mx = i, k

        def not_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return True
            return False

        left = nums[:ind_mx]
        right = nums[ind_mx + 1:][::-1]

        if not_sorted(left) or not_sorted(right) or ind_mx == n - 1: 
            return -1
        
        diff = sum(left) - sum(right) + mx

        if mx == nums[ind_mx + 1]:
            return abs(diff)

        return min(abs(diff), abs(diff - 2 * mx))