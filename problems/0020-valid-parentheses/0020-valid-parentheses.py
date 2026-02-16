class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        diction = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for br in s:
           
            if br == '(' or br == '{' or br == '[':
                stack.append(br)
            else:
                if len(stack) == 0 or stack.pop() != diction[br]:
                    return False

        return len(stack) == 0

        # O(len(s)) - time
        # O(len(s)) - space