class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        diction = {}
        tSet = set()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in diction:
                if t[i] in tSet:
                    return False
                else:
                    diction[s[i]] = t[i]
                    tSet.add(t[i])
            else:
                if t[i] != diction[s[i]]:
                    return False
            
        return True
        # O(len(s)) - time
        # O(len(s)) - memory