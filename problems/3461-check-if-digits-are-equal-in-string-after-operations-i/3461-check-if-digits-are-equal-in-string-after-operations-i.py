class Solution:
    def hasSameDigits(self, s: str) -> bool:

        digits = [int(c) for c in s] # O(n) space

        while(len(digits) > 2): # O (n)
            new_digits = []

            for i in range(len(digits) - 1): # O(n)
                d = (digits[i] + digits[i + 1]) % 10
                # digits = digits[:i] + [d] + digits[i + 1:] # O(n)
                new_digits.append(d) # O(1)
                
                # if i == len(digits) - 2:
                #     digits = digits[:i + 1] # O(n)
            digits = new_digits

        return digits[0] == digits[1]
        # time complexity O(n^2)
        # space complexity O(n) each loop I create string s