class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def longest_seq_end_at(i):
            if i not in memo:
                mx = 1
                for before_i in range(i):
                    if nums[before_i] < nums[i]:
                        mx = max(mx, longest_seq_end_at(before_i) + 1)
                        
                memo[i] = mx
            return memo[i]

        mx = 0
        for i in range(n):
            mx = max(mx, longest_seq_end_at(i))
            
        return mx