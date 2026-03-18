class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = defaultdict(int)
        for ch in s:
            d1[ch] += 1
        d2 = defaultdict(int)
        for ch in t:
            if ch not in d1:
                return ch
            else:
                d2[ch] += 1
                if d1[ch] < d2[ch]:
                    return ch
        
        return ''
        # O(n) - time
        # O(n) - space