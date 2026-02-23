class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = []

        diction = {}

        def fromSameShiftingSeq(word1, word2):
            diff = (ord(word1[0]) - ord(word2[0])) % 26
            for i in range(len(word1)):
                if (ord(word2[i]) - ord('a')+ diff) % 26 != ord(word1[i]) - ord('a'):
                    return False
            return True

        for string in strings:
            length = len(string)
            if length in diction:
                wasAdded = False
                for i,group in enumerate(diction[length]):
                    first_word = group[0]
                    if fromSameShiftingSeq(first_word, string):
                        diction[length][i].append(string)
                        wasAdded = True
                        break
                if not wasAdded:
                    diction[length].append([string])
            else:
                diction[length] = [[string]]

        for number, ls in diction.items():
            ans.extend(ls)
        
        return ans

        # O(n^2 * m) - time (n - strings length, m - max_string length)
        # O(m * n) - space