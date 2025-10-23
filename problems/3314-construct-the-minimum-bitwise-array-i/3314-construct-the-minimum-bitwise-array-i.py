class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        for i, n in enumerate(nums):
            found = False
            for j in range(n//2, n):
                if j | (j + 1) == n:
                    result[i] = j
                    found = True
                    break
            if not found:
                result[i] = -1
            
        return result
        # O(n^2) - time
        # O(n) - space