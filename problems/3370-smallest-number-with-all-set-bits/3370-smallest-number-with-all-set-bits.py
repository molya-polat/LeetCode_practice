class Solution:
    def smallestNumber(self, n: int) -> int:
        return min(2 ** k - 1 for k in range(1, 11) if 2 ** k > n)