class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        set_remainders = {}
        sm = 0
        for i, n in enumerate(nums):
            sm += n
            if sm % k == 0 and i > 0:
                return True
            remainder = sm % k
            if remainder in set_remainders and (i - set_remainders[remainder]) >= 2:
                return True
            if remainder not in set_remainders:
                set_remainders[remainder] = i
           
        
        return False
        # O(n) - time
        # O(n) - space