class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        med = (left + right) // 2
        while left < right:
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/med)
            
            if hours_spent > h:
                left = med + 1
            
            if hours_spent <= h:
                right = med

            med = (left + right) // 2
        
        return med
        # O(n logm) - time
        # O(1) - space