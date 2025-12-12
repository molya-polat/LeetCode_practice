class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def max_Alice_score(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if end == start:
                memo[(start, end)] = 0
                return 0
            max_score = 0
            if (end - start) % 2 == 0:
                case1_score = piles[start] + max_Alice_score(start + 1, end)
                case2_score = piles[end - 1] + max_Alice_score(start, end - 1)
                max_score = max(case1_score, case2_score)
            else:
                case1_score = -piles[start] + max_Alice_score(start + 1, end)
                case2_score = max_Alice_score(start, end - 1) - piles[end - 1]
                max_score = min(case1_score, case2_score)

            memo[(start, end)] = max_score
            return max_score
                

        return max_Alice_score(0, len(piles)) > 0
# O(n*n) - time
# O(n*n) - memory