class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        mem = [0 for _ in range(n + 1)]
        mem[0] = 0
        mem[1] = 1
        mem[2] = 1
        for i in range(3, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3]

        return mem[n]        
        # O(n) - time
        # O(n) - space