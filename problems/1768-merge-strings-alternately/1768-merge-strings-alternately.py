class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxL = max(len(word1), len(word2))
        result = ""
        for i in range(maxL):
            if i < len(word1):
                result += word1[i]
            
            if i < len(word2):
                result += word2[i]
        return result
# O(max(n, m)) - time
# O(n + m) - space