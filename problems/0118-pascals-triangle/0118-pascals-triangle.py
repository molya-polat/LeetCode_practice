class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 3:
            pascalRows = [[1]] if numRows == 1 else [[1], [1,1]]
            return pascalRows

        pascalRows = [[1], [1, 1]]
        for row in range(2, numRows):
            nextRow = [1]
            for i in range(1, row):
                nextRow.append(pascalRows[row - 1][i - 1] + pascalRows[row -1][i])
            # nextRow = nextRow + [1]
            nextRow.append(1)
            pascalRows.append(nextRow)

        return pascalRows

        # O(n^2) - time complexity
        # O(n^2) - space complexity