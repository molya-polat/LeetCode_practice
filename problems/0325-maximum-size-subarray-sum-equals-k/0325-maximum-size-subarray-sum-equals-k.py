class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {}
        sm = 0
        max_length = 0
        for i, n in enumerate(nums):
            sm += n
            if sm == k:
                max_length = max(max_length, i + 1)
            if sm not in prefix_sum:
                prefix_sum[sm] = i + 1
            if sm - k in prefix_sum:
                max_length = max(max_length, i - prefix_sum[sm - k] + 1)
        
        return max_length

        # O(n) - time
        # O(n) - space