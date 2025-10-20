class Solution:
    def possibleStringCount(self, word: str) -> int:
        possibleStrings = 1
        newCh = ''
        counter = 0
        for ch in word:
            if newCh != ch:
                newCh = ch
                possibleStrings += counter
                counter = 0
            else:
                counter += 1
        if counter != 0:
            possibleStrings += counter

        return possibleStrings

        # O(n) - time compl
        # O(1) - space compl