class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_ans = max(nums)

        cur_pref = 0
        mn_pref = 0

        for a in nums:

            cur_pref += a

            possible_ans = cur_pref - mn_pref
            mx_ans = max(possible_ans, mx_ans)

            mn_pref = min(cur_pref, mn_pref)

        return mx_ans