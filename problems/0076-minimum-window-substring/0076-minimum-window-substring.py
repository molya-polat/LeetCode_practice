class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct_s = defaultdict(int)
        ct_t = Counter(t)

        right = 0

        def good():
            for c in ct_t:
                if ct_t[c] > ct_s[c]:
                    return False
            return True

        ans = (10 ** 9, -1)

        for i in range(0, len(s)):
            while right < len(s) and not good():
                ct_s[s[right]] += 1
                right += 1

            if good() and right - i < ans[0]:
                ans = (right - i, i)

            ct_s[s[i]] -= 1

        if ans[0] == 10 ** 9:
            return ''

        return s[ans[1] : ans[0] + ans[1]]


        # O(n) - time complexity
        # O(1) - space complexity