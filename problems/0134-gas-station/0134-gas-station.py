class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sm = 0
        minSm = 10**9
        index = 0
        for i in range(len(gas)):
            if sm < minSm:
                minSm = sm
                index = i
            sm += gas[i] - cost[i]

        if sm < 0:
            return -1

        return index
# O(n) - time
# O(1) - space