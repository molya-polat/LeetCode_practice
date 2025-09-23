from collections import Counter
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        chars = set(s)
        if len(chars) <= k:
            return 0
        dictionary = Counter(s)
        diff = len(dictionary) - k
        sortedValues = sorted(dictionary.values())
        minDel = sum(sortedValues[:diff])
        return minDel