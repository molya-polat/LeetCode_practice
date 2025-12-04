class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        diction = {}
        min_dist = 10 ** 9
        for i, n in enumerate(nums):
            if n not in diction:
                diction[n] = [i]
            else:
                if len(diction[n]) >= 2:
                    temp_l = len(diction[n])
                    min_dist = min(min_dist, 2 * (i - diction[n][temp_l - 2]))
                diction[n].append(i)

        if min_dist == 10 ** 9:
            return -1    
        return min_dist

        # O(n) - time
        # O(n) - memory