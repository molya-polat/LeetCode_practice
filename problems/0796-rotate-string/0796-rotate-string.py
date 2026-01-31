class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            new_s = s[i + 1:] + s[:i + 1]
            if new_s == goal:
                return True
        
        return False

        # O(len(s)) - time
        # O(len(s)^2) - space