class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def isPower(n):
            if n == 1:
                return True
            elif n % 2 != 0 or n == 0:
                return False
            return isPower(n // 2)
        return isPower(n)
        # O(logn) - time compl
        # O(1) - space compl