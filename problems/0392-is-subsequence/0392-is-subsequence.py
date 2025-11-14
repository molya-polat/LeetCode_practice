class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        sIndex = 0
        for ch in t:
            if ch == s[sIndex]:
                sIndex += 1
                if sIndex == len(s):
                    return True

        if sIndex < len(s):
            return False
        return False   

    #O(len(t)) - time
    # O(1) - memory