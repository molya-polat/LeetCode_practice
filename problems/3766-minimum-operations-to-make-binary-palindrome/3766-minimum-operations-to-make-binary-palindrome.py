class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []

        def isPalindrome(n):
            bin_n = bin(n)[2:]
            bin_n_str = str(bin_n)
            reversed_bin_n_str = ''.join(reversed(bin_n_str))
            return reversed_bin_n_str == bin_n_str

        for n in nums:
            oper = 0
            incr = 0
            while True:
                if isPalindrome(n - incr) or isPalindrome(n + incr):
                    break
                oper += 1
                incr += 1
            
            ans.append(oper)
        
        return ans

        # O(n * n) - time?
        # O(n) - memory