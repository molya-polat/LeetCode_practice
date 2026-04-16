class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        ans = [0 for _ in range(n)]
        visited = set()
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    ans[i] += matrix[i][j]
                    ans[j] += matrix[i][j]
                    visited.add((j, i))
                    visited.add((i, j))
            
        return ans

        # O(n * n) - time
        # O(n) - space