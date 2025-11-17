class Solution:
    def romanToInt(self, s: str) -> int:
        diction = {}
        diction['I'] = 1
        diction['V'] = 5
        diction['X'] = 10
        diction['L'] = 50
        diction['C'] = 100
        diction['D'] = 500
        diction['M'] = 1000

        ans = 0
        prev = -1
        for ch in s:
            if prev != -1 and (diction[ch] // prev == 5 or diction[ch] // prev == 10):
                tmp = diction[ch] - prev
                ans = ans - prev
                ans += tmp
            else:
                ans += diction[ch]
            prev = diction[ch]
        return ans

        # O(len(s)) - time
        # O(1) - memory