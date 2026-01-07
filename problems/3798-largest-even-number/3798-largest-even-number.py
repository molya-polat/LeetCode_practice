class Solution:
    def largestEven(self, s: str) -> str:
        n = int(s)
        while n % 2 == 1:
            n = n // 10
        
        if n == 0:
            return ""
        return str(n)

        # O(log n) - time complexity
        # O(1) - memory