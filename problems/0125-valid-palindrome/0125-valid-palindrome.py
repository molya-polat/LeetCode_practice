class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for ch in s:
            chl = ch.lower()
            if ord(chl) > 96 and ord(chl) < 123 or ord(chl) > 47 and ord(chl) < 58:
                word += chl
        length = len(word) 
        for i in range(length//2):
            if word[i] != word[length - i - 1]:
                return False
        return True
        # O(len(s)) - time
        # O(len(s)) - memory