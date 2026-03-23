class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:   
        ans = [] 
        def isAnagram(word1, word2):
            diction1 = defaultdict(int)
            diction2 = defaultdict(int)
            for ch in word1:
                diction1[ch] += 1
            for ch in word2:
                diction2[ch] += 1
            for ch, ct in diction1.items():
                if ch not in diction2:
                    return False
                if diction1[ch] != diction2[ch]:
                    return False
            for ch, ct in diction2.items():
                if ch not in diction1:
                    return False
                if diction2[ch] != diction1[ch]:
                    return False
            
            
            return True
        current = 0
        for i in range(1, len(words)):
            isAnagrams = isAnagram(words[current], words[i])
            if not isAnagrams:
                ans.append(words[current])
                current = i
        ans.append(words[current])
        return ans

# O(n) - time
# O(n) - space