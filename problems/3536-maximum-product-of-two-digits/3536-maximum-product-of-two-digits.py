class Solution:
    def maxProduct(self, n: int) -> int:
        dictDigits = {}
        while n > 0:
            digit = n % 10
            if digit in dictDigits:
                dictDigits[digit] += 1
            else:
                dictDigits[digit] = 1
            n = n // 10
        maxDigit = max(dictDigits.keys())
        if dictDigits[maxDigit] > 1: #appears more than once
            return maxDigit * maxDigit
        dictDigits.pop(maxDigit)
        maxDigitSecond = max(dictDigits.keys())
        return maxDigit * maxDigitSecond