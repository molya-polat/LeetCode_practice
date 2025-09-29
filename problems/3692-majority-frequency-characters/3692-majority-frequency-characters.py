class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        dictionary = defaultdict(int)
        freqDict = defaultdict(str)

        for ch in s:
            dictionary[ch] += 1
        for key,value in dictionary.items():
            freqDict[value] += key

        maxGroupSize = 0
        output = ''
        for freq, characters in sorted(freqDict.items(), reverse = True):
            if maxGroupSize < len(characters):
                maxGroupSize = len(characters)
                output = characters
            
        return output