class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        maxProfit = 0
        minLeft = prices[0]
        for i in range(1, len(prices)):
            minLeft = min(minLeft, prices[i - 1])
            if prices[i] - minLeft < maxProfit:
                result += maxProfit
                maxProfit = 0
                minLeft = prices[i]
            else:
                maxProfit = prices[i] - minLeft
        if maxProfit != 0:
            result += maxProfit
        
        return result
        # O(n) - time compl
        # O(1) - space compl