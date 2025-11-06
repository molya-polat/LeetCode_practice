class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(s)
        tSort = sorted(t)

        return sSorted == tSort
        # O(n logn) - time
        # O(n) - memory