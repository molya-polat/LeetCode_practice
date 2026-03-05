class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_i = set()
        for i,ch in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif ch == ")":
                if len(stack) == 0:
                    remove_i.add(i)
                else:
                    stack.pop()
        if len(stack) > 0:
            while stack:
                ch, index = stack.pop()
                remove_i.add(index)

        ans = ""
        for i in range(len(s)):
            if i not in remove_i:
                ans += s[i]
        
        return ans
        # O(n) - time
        # O(n) - space