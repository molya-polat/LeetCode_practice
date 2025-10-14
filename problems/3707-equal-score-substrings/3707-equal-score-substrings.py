class Solution:
    def scoreBalance(self, s: str) -> bool:
        sumLeft = 0
        sumRight = 0
        length = len(s)
        sumLeftList = [0 for _ in range(len(s))]
        sumRightList = [0 for _ in range(len(s))]
        for i, ch in enumerate(s):
            sumLeft += ord(ch) - 96
            sumLeftList[i] = sumLeft
            sumRight += ord(s[length - 1 - i]) - 96
            sumRightList[length - 1 - i] = sumRight
            
        for i in range(len(s) - 1):
            if sumLeftList[i] == sumRightList[i + 1]:
                return True
        
        return False

        # O(n) - time compl
        # O(n) - space compl