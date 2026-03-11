from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited_queued = set()
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < n
        queue = deque()
        queue.append((n - 1, n - 1, 1))
        visited_queued.add((n - 1, n - 1))
        while queue:
            (i, j, moves) = queue.popleft()
            if i == 0 and j == 0:
                return 1
            possible_neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for ni, nj in possible_neighbors:
                if isValid(ni, nj) and grid[ni][nj] == 0 and (ni, nj) not in visited_queued:
                    queue.append((ni, nj, moves + 1))
                    visited_queued.add((ni, nj))
                    if ni == 0 and nj == 0:
                        return moves + 1
        
        return -1
        # O(m * n) - time
        # O(m * n) - space