class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)

        def minCoins(amount):
            if amount == 0:
                return 0
            for c in coins:
                if c <= amount:
                    remain = amount - c
                    temp = minCoins(remain)
                    if temp != -1:
                        ans = 1 + temp
                        print(ans)
                        return ans
            
            return -1



        return minCoins(amount)























        # INF = 1e9
        # memo = {}

        # def minimal_number_of_coins(j):
        #     if j == 0:
        #         return 0
        #     if j < 0:
        #         return INF

        #     if j in memo:
        #         return memo[j]

        #     ans = INF
        #     for c in coins:
        #         ans = min(ans, minimal_number_of_coins(j - c) + 1)

        #     memo[j] = ans
        #     return ans

        # ans = minimal_number_of_coins(amount)

        # if ans >= INF:
        #     return -1
        # else:
        #     return ans

        # # Time complexity  - O(amount * len(coins))
        # # Space complexity - O(amount)