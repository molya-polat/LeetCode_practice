class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i,price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= price:
                    ans.append(price - prices[j])
                    break
            if len(ans) < i + 1:
                ans.append(price)
        
        return ans

        # O(n^2) - time
        # O(n) - memory