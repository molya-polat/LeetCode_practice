class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def willCollapse(a, b):
            if a < 0 and b < 0 or a > 0 and b > 0 or a < 0 and b > 0:
                return False
            return True
            
        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                while stack:
                    last = stack[-1]
                    if willCollapse(last, a):
                        if abs(a) > abs(last):
                            stack.pop()
                            if not stack:
                                stack.append(a)
                                break
                        elif abs(a) == abs(last):
                            stack.pop()
                            break
                        else:
                            break
                    else:
                        stack.append(a)
                        break
        return stack

        # O(n) - time
        # O(n) - space