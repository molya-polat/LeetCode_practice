class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        prefix_sum = {-1: 0}
        sm = 0
        for i, n in enumerate(nums):
            sm += n
            prefix_sum[i] = sm

        multiply = {1: {len(nums)}}
        m = 1
        for i in range(len(nums) - 1, 0, -1):
            if m == prefix_sum[i - 1]:
                return i
            elif m > prefix_sum[i - 1]:
                break
            m = m * nums[i]
            if m not in multiply:
                multiply[m] = set()
            multiply[m].add(i)

        return -1
        # O(n) - time
        # O(n) - space