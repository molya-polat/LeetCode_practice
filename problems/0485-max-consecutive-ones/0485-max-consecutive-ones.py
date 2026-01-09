class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_number = 0
        for n in nums:
            if n == 1:
                current += 1
                max_number = max(max_number, current)
            else:
                max_number = max(max_number, current)
                current = 0
        
        return max_number

    # O(n) - time
    # O(1) - space