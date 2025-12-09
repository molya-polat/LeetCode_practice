class Solution:
    def countVowelStrings(self, n: int) -> int:
        order = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        diction = {}

        def count_strs(ch_p, n):
            if (ch_p, n) in diction:
                return diction[(ch_p, n)]
            if n == 1:
                diction[(ch_p, n)] = 5 - order[ch_p]
                return 5 - order[ch_p]
            else:
                ans = 0
                for ch in order:
                    if order[ch] >= order[ch_p]:
                        ans += count_strs(ch, n - 1)
            diction[(ch_p, n)] = ans
            return ans
        
        return count_strs('a', n)

        # O(n) - time, if not Constant O(k^2 * n) - k - order's size
        # O(n) - memory, if not Constant O(k * n)