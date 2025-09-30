class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Solution 1
        # for fruit in fruits:
        #     i = 0
        #     while i < len(baskets):
        #         if baskets[i] >= fruit:
        #             baskets.pop(i)
        #             break
        #         else:
        #             i += 1
        # return len(baskets)

        # Solution 2
        occupied = [False] * len(baskets)            
        for fruit in fruits:
            for i in range(len(baskets)):
                if not occupied[i] and baskets[i] >= fruit:
                    occupied[i] = True
                    break
        return len(fruits) - sum(occupied)

        # What are the time complexities?