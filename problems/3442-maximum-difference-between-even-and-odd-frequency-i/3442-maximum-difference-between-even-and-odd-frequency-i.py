class Solution:
    def maxDifference(self, s: str) -> int:
        diction = defaultdict(int)
        for ch in s:
            diction[ch] += 1
        maxOdd = 0
        minEven = 10**6
        for ch, freq in diction.items():
            if freq % 2 == 0:
                minEven = min(minEven, freq)
            else:
                maxOdd = max(maxOdd, freq)
        
        return maxOdd - minEven
        # O(n) - time complexity
        # O(n) - space complexity