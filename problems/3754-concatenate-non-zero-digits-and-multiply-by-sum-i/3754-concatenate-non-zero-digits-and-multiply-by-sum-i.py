class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sm = 0
        x = 0
        t = 0
        while n > 0:
            r = n % 10
            if r != 0:
                x += 10 ** t * r
                sm += r
                t += 1
            n = n // 10
        
        return x * sm
        # O(logn) - time
        # O(1) - memory