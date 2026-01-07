class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        newstr = s[:k]
        newstr_reversed = "".join(reversed(newstr))
        return newstr_reversed + s[k:]

        # O(1) - time complexity
        # O(n) - memory