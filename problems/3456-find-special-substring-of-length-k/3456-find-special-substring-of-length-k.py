class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) == 1 and k == 1:
             return True
        currentCh = s[0]
        counter = 0
        specialCh = ''
        for i, ch in enumerate(s):
            if counter == k:
                if ch is not specialCh:
                    return True
                else:
                    counter += 1
            elif counter < k:
                if ch == currentCh:
                    counter += 1
                    if counter == k:
                        specialCh = ch
                        if i == len(s) - 1:
                            return True
                else:
                    counter = 1
                    currentCh = ch
            else:
                counter = 1
                currentCh = ch

        if counter == k:
            return True
        else:
            return False
# O(n) - time compl
# O(1) - space compl