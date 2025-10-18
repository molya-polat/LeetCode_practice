class Solution:
    def isBalanced(self, num: str) -> bool:
        evenSum = 0
        oddSum = 0
        for i, ch in enumerate(num):
            if i % 2 == 0:
                evenSum += int(ch)
            else:
                oddSum += int(ch)
        return evenSum == oddSum
        # O(n) - time compl
        # O(1) - space compl