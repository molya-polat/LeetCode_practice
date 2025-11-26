class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        diction = defaultdict(int)
        maxN = -1
        maxC = -10 ** 9
        for n in nums:
            diction[n] += 1
            if maxC < diction[n]:
                maxC = diction[n]
                maxN = n

        return maxN
        # O(n) - time
        # O(n) - memory