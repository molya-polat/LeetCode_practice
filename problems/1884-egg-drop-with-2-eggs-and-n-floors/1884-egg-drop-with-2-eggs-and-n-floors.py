class Solution:
    def twoEggDrop(self, n: int) -> int:
        INF = 10 ** 9
        memo = {}

        def min_moves_with_certainty(below):
            if below not in memo:
                if below == n:
                    memo[below] = 0
                else:
                    mn_i_moves = INF
                    for i in range(below + 1, n + 1):
                        steps_not_break = min_moves_with_certainty(i)
                        steps_if_break = i - below - 1
                        worst_case_scenario = 1 + max(steps_not_break, steps_if_break)
                        mn_i_moves = min(mn_i_moves, worst_case_scenario)
                    memo[below] = mn_i_moves
            return memo[below]

        return min_moves_with_certainty(0)