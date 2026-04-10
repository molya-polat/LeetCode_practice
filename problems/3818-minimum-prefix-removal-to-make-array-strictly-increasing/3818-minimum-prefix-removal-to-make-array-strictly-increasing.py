class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        ans = 0
        increasing_len = 0
        for i in range(len(nums) -1):
            if nums[i] >= nums[i + 1]:
                ans += increasing_len + 1
                increasing_len = 0
            else:
                increasing_len += 1
        
        return ans

# O(n) - time
# O(1) - space