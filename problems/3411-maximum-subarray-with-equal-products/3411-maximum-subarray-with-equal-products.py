class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        for length in range(len(nums), 0, -1):
            start = 0
            while True:
                if start + length > len(nums):
                    break
                product = nums[start]
                gcd_comp = nums[start]
                lcm_comp = nums[start]
                for i in range(start + 1, start + length):
                    product = product * nums[i]
                    gcd_comp = gcd(max(nums[i], gcd_comp), min(nums[i], gcd_comp))
                    lcm_comp = abs(nums[i] * lcm_comp) // gcd(max(lcm_comp, nums[i]), min(lcm_comp, nums[i]))
                if product == gcd_comp * lcm_comp:
                    return length
                start += 1
        
        return []
        # O(n^3) - time compl
        # O(1) - space compl