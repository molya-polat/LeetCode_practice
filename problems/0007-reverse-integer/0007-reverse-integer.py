class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        power = 0 
        new_x = abs(x)
        while new_x > 0:
            remainder = new_x % 10
            result = result * 10 + remainder
            power += 1
            new_x = new_x // 10
        
        if result > 2 ** 31 - 1:
            return 0
        if x < 0:
            return -result
        return result

# O(len(x)) - time
# O(1) - space