class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MINF = -1e9
        n = len(prices)

        SOLD_THEN_COOLDOWN = -1
        CAN_BUY = 0
        BOUGHT_NEED_TO_SELL = 1

        memo = {}

        def max_profit(i, state):
            if i == n:
                if state == CAN_BUY or state == SOLD_THEN_COOLDOWN:
                    return 0
                else:
                    return MINF

            if (i, state) in memo:
                return memo[(i, state)]
            
            if state == CAN_BUY: # i = n - 1
                ans = max(
                        max_profit(i + 1, BOUGHT_NEED_TO_SELL) - prices[i],
                        max_profit(i + 1, CAN_BUY) # i = n, CAN_BUY
                    )
            elif state == BOUGHT_NEED_TO_SELL: # i = n - 1
                ans = max(
                        max_profit(i + 1, SOLD_THEN_COOLDOWN) + prices[i], # i = n
                        max_profit(i + 1, BOUGHT_NEED_TO_SELL) 
                    )
            else:
                ans = max_profit(i + 1, CAN_BUY)

            memo[(i, state)] = ans
            return ans

        return max_profit(0, CAN_BUY)

        # Time complexity  - O(n)
        # Space complexity - O(n)