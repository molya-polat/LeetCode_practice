class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pList = p.split('*')
        if pList[0] in s:
            s = s[s.find(pList[0]) + len(pList[0]):]
            if pList[1] in s:
                return True
        return False

        # O(n) - time compl
        # O(1) - space compl