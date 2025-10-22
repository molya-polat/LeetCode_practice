class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        counter = 1
        m = k * counter
        presentMultiples = set()
        for n in nums:
            if n % k == 0:
                presentMultiples.add(n)
            if n == m:
                while m in presentMultiples:
                    counter += 1
                    m = counter * k

        return m
        # O(n^2) - time compl
        # O(n) - space compl