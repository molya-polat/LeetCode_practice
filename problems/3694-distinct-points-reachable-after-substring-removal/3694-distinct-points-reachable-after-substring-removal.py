class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        positionSet = set()
        positionList = []
        x, y = 0, 0
        for ch in s:
            if ch == 'U':
                y = y + 1
            elif ch == 'D':
                y = y - 1
            elif ch == 'L':
                x = x - 1
            else:
                x = x + 1
            positionList.append((x, y))

        
        for i in range(len(s) - k + 1): 
            removeStrStartX = positionList[i - 1][0] if i > 0 else 0
            removeStrStartY = positionList[i - 1][1] if i > 0 else 0

            removeStrEndX = positionList[i + k - 1][0]
            removeStrEndY = positionList[i + k - 1][1]

            newX = x - removeStrEndX + removeStrStartX
            newY = y - removeStrEndY + removeStrStartY

            positionSet.add((newX, newY))

        return len(positionSet)

        # O(n) - time complexity
        # O(n) - space complexity