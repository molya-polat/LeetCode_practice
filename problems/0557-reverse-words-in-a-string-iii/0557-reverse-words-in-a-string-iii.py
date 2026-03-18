class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        def reverse(word):
            res = ''
            for i in range(len(word) - 1, -1, -1):
                res += word[i]
            res += " "
            return res
        current_ans = ''    
        for ch in s:
            if ch == ' ':
                ans += reverse(current_ans)
                current_ans = ''
            else:
                current_ans += ch
        ans += reverse(current_ans)
        ans = ans[:-1]
        return ans
    
    # O(n) - time
    # O(1) - space