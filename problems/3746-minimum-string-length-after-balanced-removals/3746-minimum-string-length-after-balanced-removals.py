class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = 0
        b = 0
        for ch in s:
            if ch == 'a':
                a += 1
            else:
                b += 1
        
        return abs(a - b)

        # O(len(s)) - time
        # O(1) - memory