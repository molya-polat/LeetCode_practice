class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_reversed = "".join(reversed(str(n)))
        return abs(n - int(n_reversed))

        # O(1) - time
        # O(log n) - memory