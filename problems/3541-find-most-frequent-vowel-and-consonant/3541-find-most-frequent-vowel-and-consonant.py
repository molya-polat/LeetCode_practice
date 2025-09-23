from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        dictionary = {}
        for c in s:
            if c in dictionary:
                dictionary[c] += 1
            else:
                dictionary[c] = 1
        setVowels = {'a', 'e', 'i', 'o', 'u'}

        maxVowelFrequency = 0
        maxConsonantFrequency = 0
        for key in dictionary:
            if key in setVowels:
                maxVowelFrequency = max(maxVowelFrequency, dictionary[key])
            else:
                maxConsonantFrequency = max(maxConsonantFrequency, dictionary[key])

        return maxVowelFrequency + maxConsonantFrequency