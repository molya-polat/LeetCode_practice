class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        tenPower = 0
        while n > 0:
            newComponent = (n % 10) * (10 ** tenPower)
            if newComponent != 0:
                result.insert(0, newComponent)
            tenPower += 1
            n = n // 10
        return result