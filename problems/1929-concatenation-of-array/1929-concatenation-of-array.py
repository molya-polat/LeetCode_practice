class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(2 * len(nums))]
        n = len(nums)
        for i in range(2 * n):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - n]
            

        return ans

        # O(n) - time
        # O(n) - memory