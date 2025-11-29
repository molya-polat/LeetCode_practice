class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:]
        binary_reversed = binary[::-1]
        flips = 0
        for i in range(len(binary)):
            if binary[i] != binary_reversed[i]:
                flips += 1

        return flips
        # O(len(binary)) - time
        # O(len(binary)) - memory