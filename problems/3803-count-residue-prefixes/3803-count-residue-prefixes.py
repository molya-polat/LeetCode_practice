class Solution:
    def residuePrefixes(self, s: str) -> int:
        current_prefix = ''
        count = 0
        for ch in s:
            current_prefix += ch
            st_chars = set(current_prefix)
            if len(current_prefix) % 3 == len(st_chars):
                count += 1
        
        return count
        # O(len(s)) - time
        # O(len(s)^2) - space