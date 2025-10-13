class Solution:
    def longestBalanced(self, s: str) -> int:
        diction = defaultdict(list)
        initLength = length = len(s)
        dict1 = {}
        while length > 0:
            for i in range(initLength):
                if i + length > initLength:
                    break
                
                diction[length].append(s[i:i + length])
            length -= 1
        

        for length, strings in diction.items():
            dictionTemp = defaultdict(int)
            dict1 = defaultdict(int)
            for ch in strings[0]:
                dictionTemp[ch] += 1
            for ch, freq in dictionTemp.items():
                dict1[freq] += 1
            if dict1[dictionTemp[strings[0][0]]] * dictionTemp[strings[0][0]] == len(strings[0]):
                return len(strings[0])
            prev = strings[0]
            for i in range(1, len(strings)):
                dict1[dictionTemp[strings[i][-1]]] -= 1
                dictionTemp[strings[i][-1]] += 1
                dict1[dictionTemp[strings[i][-1]]] += 1
                dict1[dictionTemp[prev[0]]] -= 1
                dictionTemp[prev[0]] -= 1
                dict1[dictionTemp[prev[0]]] += 1
                if dict1[dictionTemp[strings[i][0]]] * dictionTemp[strings[i][0]] == len(strings[i]):
                    return len(strings[i])
                prev = strings[i]
        
        return 0

        # O(n^2) - time compl
        # O(n^2) - space compl