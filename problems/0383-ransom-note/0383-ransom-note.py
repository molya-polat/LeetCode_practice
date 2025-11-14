class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        diction = defaultdict(int)
        for ch in magazine:
            diction[ch] += 1
        for ch in ransomNote:
            if ch in diction:
                if diction[ch] == 0:
                    return False
                else:
                    diction[ch] -= 1
            else:
                return False
        
        return True
        # O(max(len(ransomNote, magazine))) - time
        # O(len(magazine)) - memory