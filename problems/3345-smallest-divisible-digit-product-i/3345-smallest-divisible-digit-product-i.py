class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            tempN = n
            while tempN > 0:
                product = product * (tempN % 10)
                tempN = tempN // 10
            
            if product % t == 0:
                return n
            n += 1

        return 0
        # O(t*logn) - time compl
        # O(1) - space compl