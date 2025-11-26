class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        diction = {}
        li = 0
        maxL = -10 ** 9
        for i, ch in enumerate(s):
            if ch not in diction:
                diction[ch] = i
                maxL = max(maxL, i - li + 1)
            else:
                if diction[ch] >= li:
                    maxL = max(maxL, i - li)
                    li = diction[ch] + 1
                else:
                    maxL = max(maxL, i - li + 1)
                diction[ch] = i
        if maxL < 0:
            return len(s)
        return maxL
        # O(len(s)) - time
        # O(len(s)) - memory