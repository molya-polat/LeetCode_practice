class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        diction = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        else:
            for i in range(len(pattern)):
                o = ord(pattern[i])
                if o in diction:
                    if diction[o] != words[i]:
                        return False
                    if diction[words[i]] != o:
                        return False
                else:
                    if words[i] in diction:
                        if diction[words[i]] != ord(pattern[i]):
                            return False
                    else:
                        diction[words[i]] = o
                    diction[o] = words[i]
        
        return True
        # O(len(pattern)) - time
        # O(len(s)) - memory