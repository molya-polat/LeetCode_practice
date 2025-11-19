class Solution:
    def customSortString(self, order: str, s: str) -> str:
        diction = defaultdict(int)
        for i, ch in enumerate(order):
            diction[ch] = i
        
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
                    if s1[i] in diction and s2[j] in diction:
                        if diction[s1[i]] < diction[s2[j]]:
                            ans += s1[i]
                            i += 1
                        else:
                            ans += s2[j]
                            j += 1
                    elif s1[i] in diction and s2[j] not in diction:
                        ans += s2[j]
                        j += 1
                    elif s1[i] not in diction and s2[j] in diction:
                        ans += s1[i]
                        i += 1
                    else:
                        ans += s1[i]
                        ans += s2[j]
                        i += 1
                        j += 1
                    
            return ans
        
        def divide(s):
            medium = len(s) // 2
            s1 = s[:medium]
            s2 = s[medium:]
            if len(s1) > 1:
                s1 = divide(s1)
            if len(s2) > 1:
                s2 = divide(s2)
            
            return merge(s1, s2)
        
        return divide(s)
        # O(n*logn) - time - n - len(s)
        # O(n*logn) - memory