class Solution:
    def minCost(self, n: int) -> int:
        memo = {}
        def findAllpossibleSplits(n):
            st = set()
            for i in range(1, n // 2 + 1):
                st.add((i, n - i))
            
            return st


        def minCostFrom(k):
            if k == 1:
                return 0
            if k == 2:
                return 1
            if k not in memo:
                min_cost = 10 ** 7
                possibleSplits = findAllpossibleSplits(k)
                for a, b in possibleSplits:
                    min_cost = min(min_cost, a * b + minCostFrom(a) + minCostFrom(b))

                memo[k] = min_cost
            
            return memo[k]
            
        return minCostFrom(n)

# O(n) - time
# O(n) - space