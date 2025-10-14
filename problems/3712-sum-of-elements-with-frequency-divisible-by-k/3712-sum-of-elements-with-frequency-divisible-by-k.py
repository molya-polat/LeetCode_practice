class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        diction = defaultdict(int)
        for num in nums:
            diction[num] += 1
        sumResult = 0
        for num, freq in diction.items():
            if freq % k == 0:
                sumResult += num * freq
        
        return sumResult
        # O(n) - time compl
        # O(n) - space compl