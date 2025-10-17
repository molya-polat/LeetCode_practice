class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = 0
        emptyBottles = 0
        while True:
            if emptyBottles - numExchange >= 0:
                emptyBottles -= numExchange
                numExchange += 1
                numBottles += 1
            elif numBottles > 0:
                bottlesDrunk += numBottles
                emptyBottles += numBottles
                numBottles = 0
            else:
                break

        return bottlesDrunk

# O(numBottles / numExchange) - time compl - ?
# O(1) - space compl