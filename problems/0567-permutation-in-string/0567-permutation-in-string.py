class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0 for _ in range(26)]
        s2_freq = [0 for _ in range(26)]

        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False

        for i in range(l1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        

        if s1_freq == s2_freq:
            return True
        
        for start in range(l2 - l1):
            s2_freq[ord(s2[start]) - ord('a')] -= 1
            s2_freq[ord(s2[start + l1]) - ord('a')] += 1

            if s1_freq == s2_freq:
                return True
            
        return False
    # O(l2) - time
    # O(1) - space

        # O()