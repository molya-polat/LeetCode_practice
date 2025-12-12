class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        INF = 10 ** 9
        min_dist = INF

        def reverse(x):
            ch_x = str(x)
            reversed_str = "".join(reversed(ch_x))
            reversed_x = int(reversed_str)

            return reversed_x

        diction = {}

        for i, n in enumerate(nums):
            if n in diction:
                min_dist = min(min_dist, abs(i - diction[n]))
            reversed_n = reverse(n)
            diction[reversed_n] = i

        if min_dist == INF:
            return -1
        return min_dist
# O(n) - time
# O(n) - memory