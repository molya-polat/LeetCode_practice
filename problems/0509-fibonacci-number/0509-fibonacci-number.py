class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibonacci(n):
            if n in memo:
                return memo[n]

            if n == 0:
                ans = 0
            elif n == 1:
                ans = 1
            else:
                ans = fibonacci(n - 1) + fibonacci(n - 2)

            memo[n] = ans
            return ans
        
        return fibonacci(n)
        # O(n) - time compl
        # O(n) - space compl
        
    
    # O(n) - time
    # O(n) - mem