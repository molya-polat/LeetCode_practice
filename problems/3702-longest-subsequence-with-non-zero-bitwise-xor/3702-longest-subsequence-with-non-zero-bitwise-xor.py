class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        length = len(nums)
        xor = 0
        allZero = True
        for i, n in enumerate(nums):
            xor = xor ^ n
            if n is not 0:
                allZero = False
        if allZero:
            return 0
        if xor != 0:
            return length

        return length - 1
        


        # O(n) - time complexity
        # O(n) - space complexity

        
# 1 2 3 4 5 6 7

# 1 2 4 6 7
# 1 2 3 7
# 5 6 7
# 4 5

# 1 2 3 = 0
# 1 2 = 1 10 = 11 = 3
# 1 1 = 0