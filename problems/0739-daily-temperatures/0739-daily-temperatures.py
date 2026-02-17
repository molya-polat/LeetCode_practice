class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        for i,t in enumerate(temperatures):
            if stack:
                temp, index = stack[-1]
                while stack and stack[-1][0] < t:
                    temp, index = stack[-1]
                    ans[index] = i - index
                    stack.pop()
            stack.append((t, i))
        
        return ans

        # O(len(temp)) - time
        # O(len(temp)) - space