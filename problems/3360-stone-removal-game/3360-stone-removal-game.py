class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        k = 10
        while n > 0 and k > 0 and n - k >= k - 1:
            n = n - k
            k -= 1
        return True if k % 2 == 0 else False
# time complexity - O(1)
# space complexity - O(1)