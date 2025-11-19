class Solution:
    def frequencySort(self, s: str) -> str:
        diction = {}
        for i, ch in enumerate(s):
            if ch in diction:
                c = diction[ch][0]
                i = diction[ch][1]
                diction[ch] = (c + 1, i)
            else:
                diction[ch] = (1, i)

        def merge(s1, s2):
            ans = ''
            i, j = 0, 0
            while i < len(s1) or j < len(s2):
                if i >= len(s1) and j < len(s2):
                    ans += s2[j]
                    j += 1
                elif j >= len(s2) and i < len(s1):
                    ans += s1[i]
                    i += 1
                else:
                    if diction[s1[i]][0] == diction[s2[j]][0]:
                        if diction[s1[i]][1] < diction[s2[j]][1]:
                            ans += s1[i]
                            i += 1
                        else:
                            ans += s2[j]
                            j += 1
                    else:
                        if diction[s1[i]][0] > diction[s2[j]][0]:
                            ans += s1[i]
                            i += 1
                        else:
                            ans += s2[j]
                            j += 1
            
            return ans

        def divide(s):
            med = len(s) // 2
            s1 = s[:med]
            s2 = s[med:]
            if len(s1) > 1:
                s1 = divide(s1)
            if len(s2) > 1:
                s2 = divide(s2)
            return merge(s1, s2)

        return divide(s)
        # O(n*logn) - time, n - len(s)
        # O(n*logn) - memory