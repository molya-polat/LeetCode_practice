class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length = len(s)
        p_length = len(p)
        if p_length > s_length:
            return []
        p_letters = [0 for _ in range(26)]
        s_letters = [0 for _ in range(26)]

        for i in range(p_length):
            p_letters[ord(p[i]) - ord('a')] += 1
            s_letters[ord(s[i]) - ord('a')] += 1
        
        ans = []
        if p_letters == s_letters:
                ans.append(0)
        for j in range(1, s_length - p_length + 1):
            s_letters[ord(s[j - 1]) - ord('a')] -= 1
            s_letters[ord(s[j + p_length - 1]) - ord('a')] += 1
            if p_letters == s_letters:
                ans.append(j)
        
        
        return ans

        # O(n) - time
        # O(1) - space