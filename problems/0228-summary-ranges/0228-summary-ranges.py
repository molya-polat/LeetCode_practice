class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = [str(nums[0])]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - prev != 1:
                if int(ans[len(ans) - 1]) != prev:
                    ans[len(ans) - 1] += "->"
                    ans[len(ans) - 1] += str(prev)
                ans.append(str(nums[i]))
            else:
                if i == len(nums) - 1:
                    ans[len(ans) - 1] += "->"
                    ans[len(ans) - 1] += str(nums[i])
            prev = nums[i]

        return ans
        # O(n) - time
        # O(n) - memory