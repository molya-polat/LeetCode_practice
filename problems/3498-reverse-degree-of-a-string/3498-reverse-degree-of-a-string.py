class Solution:
    def reverseDegree(self, s: str) -> int:
        # keys = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        # values = [i for i in range(26, 0, -1)]
        # dictionary = dict(zip(keys, values))
        reverseDegree = 0
        for i, ch in enumerate(s):
            reverseDegree += (i + 1) * (26 + ord('a') - ord(ch))
        return reverseDegree