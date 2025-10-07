class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # k_balanced_str = ""
        arr = []
        for i in range(k):
            arr.append('(')
            # k_balanced_str = k_balanced_str + "("
        for i in range(k):
            arr.append(')')
            # k_balanced_str = k_balanced_str + ")"
        k_balanced_str = ''.join(arr)

        while k_balanced_str in s:
            # s = s.replace(k_balanced_str, "", 1)
            s = s.replace(k_balanced_str, "")

        return s
        
        # O(n^2) - time complexity
        # O(n) - space complexity