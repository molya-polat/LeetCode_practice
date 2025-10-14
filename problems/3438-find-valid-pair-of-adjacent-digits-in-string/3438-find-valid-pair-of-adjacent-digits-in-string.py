class Solution:
    def findValidPair(self, s: str) -> str:
        diction = defaultdict(int)
        # diction_index_pair = defaultdict(str)
        for i, digitCh in enumerate(s):
            diction[digitCh] += 1
            # diction_index_pair[i] += digitCh
            # if i > 0:
            #     diction_index_pair[i - 1] += digitCh
            
        validDigitsCh = set()



        for ch, freq in diction.items():
            if freq == int(ch):
                validDigitsCh.add(ch)
        # for index, pair in diction_index_pair.items():
        for index in range(len(s) - 1):
            # pair = [s[index], s[index + 1]]
            pair = s[index:index + 2]

            if pair[0] in validDigitsCh and pair[1] in validDigitsCh and pair[0] != pair[1]:
                return pair

        return ''

    # O(n) - time compl
    # O(n) - space compl