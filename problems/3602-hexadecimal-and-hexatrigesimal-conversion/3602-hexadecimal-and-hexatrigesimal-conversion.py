class Solution:
    def concatHex36(self, n: int) -> str:
        nSquared = n * n
        nCubed = n * n * n

        keys = [i for i in range (0, 36)]
        values = [chr(i) for i in range(ord('0'), ord('9') + 1)]
        values += [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        dictionary = dict(zip(keys, values))
        
        firstPart = ""
        secondPart = ""
        while nSquared >= 16:
            remainder = nSquared % 16
            firstPart = firstPart + dictionary[remainder]
            nSquared = nSquared // 16
        firstPart = firstPart + dictionary[nSquared]
        firstPart = firstPart[::-1] # reversed

        while nCubed >= 36:
            remainder = nCubed % 36
            secondPart = secondPart + dictionary[remainder]
            nCubed = nCubed // 36
        secondPart = secondPart + dictionary[nCubed]
        secondPart = secondPart[::-1]

        return firstPart + secondPart