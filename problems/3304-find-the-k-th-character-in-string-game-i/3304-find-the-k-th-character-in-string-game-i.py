class Solution:
    def kthCharacter(self, k: int) -> str:
        startStr = 'a'
        while len(startStr) < k:
            newStr = ''
            for ch in startStr:
                nextCh = chr(ord(ch) + 1)
                newStr += nextCh
            startStr += newStr
        
        return startStr[k - 1]
        # O(k*logk) - time
        # O(k) - space