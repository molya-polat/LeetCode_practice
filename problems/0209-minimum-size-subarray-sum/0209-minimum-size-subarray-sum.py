class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        li, i = 0, 0
        sm = 0
        mn_l = 10 ** 9
        updateSum = True
        while i < len(nums) and li < len(nums):
            if updateSum:
                sm += nums[i]
            if sm >= target:
                mn_l = min(mn_l, i - li + 1)
                sm -= nums[li]
                li += 1
                updateSum = False
            else:
                updateSum = True
                i += 1
        if mn_l > len(nums):
            return 0
        return mn_l

        # O(n) - time
        # O(1) - memory