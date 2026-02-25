class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = 10**9
        for price in prices:
            max_profit = max(max_profit, price - current_min)
            current_min = min(price, current_min)
        
        return max_profit












        # maxProfit = 0
        # minLeft = 10**8
        # for i in range(1, len(prices)):
        #     if i == 1:
        #         minLeft = min(prices[i - 1], prices[i])
        #     else:
        #         minLeft = min(minLeft, prices[i - 1])
            
        #     maxProfit = max(maxProfit, prices[i] - minLeft)
        
        # return maxProfit
# O(n) - time compl
# O(1) - space compl