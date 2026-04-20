class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            mx = 0
            for j in range(0, i + 1):
                mx = max(mx, nums[j])
            
            mn = 10 ** 9 + 1
            for p in range(i, len(nums)):
                mn = min(mn, nums[p])
            
            if mx - mn <= k:
                return i
        
        return -1

        # O(n ^ 2) - time
        # O(1) - space