class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        odds = 0
        evens = 0
        for n in nums1:
            if n % 2 == 0:
                evens += 1
            else:
                odds += 1
        
        if evens == 0 or odds == 0:
            return True
        return True