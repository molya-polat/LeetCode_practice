class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dist = 10 ** 9

        diction = {}
        for i, n in enumerate(nums):
            if n in diction:
                diction[n].append(i)
            else:
                diction[n] = [i]
        
        for indices in diction.values():
            if len(indices) >= 3:
                for i in range(len(indices)):
                    for j in range(i + 1, len(indices)):
                        for k in range(j + 1, len(indices)):

                            min_dist = min(min_dist, abs(indices[i] - indices[j]) + abs(indices[i] - indices[k]) + abs(indices[j] - indices[k]))

        if min_dist == 10 ** 9:
            return -1    
        return min_dist

        # O(n^3) - time
        # O(n) - memory