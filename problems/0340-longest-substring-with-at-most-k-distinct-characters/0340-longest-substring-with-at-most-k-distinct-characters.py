class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_length = 0
        diction = {}
        start = 0
        for end in range(len(s)):
            if s[end] in diction:
                diction[s[end]] += 1
            else:
                diction[s[end]] = 1
            
            while len(diction) > k:
                diction[s[start]] -= 1
                if diction[s[start]] == 0:
                    diction.pop(s[start])
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length

# O(n) - time
# O(n) - space