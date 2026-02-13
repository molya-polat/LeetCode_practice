from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def is_fully_rotten():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return False
            
            return True

        if is_fully_rotten():
            return 0
        visited_or_queued = set()


        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def node2neighbors(node):
            (i, j) = node
            neighbors = []
            possible = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for ni, nj in possible:
                if is_valid(ni, nj) and grid[ni][nj] == 1 and (ni, nj) not in visited_or_queued:
                    neighbors.append((ni, nj))
            
            return neighbors

        queue = deque()
        def bfs():
            current_minute = 0
            while len(queue) > 0:
                i, j, minute = queue.popleft()

                neighbors = node2neighbors((i, j))

                for to in neighbors:
                    if to not in visited_or_queued:
                        visited_or_queued.add(to)
                        queue.append((to[0], to[1], minute + 1))
                        grid[to[0]][to[1]] = 2
                current_minute = minute
            
            return current_minute
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i,j) not in visited_or_queued:
                    queue.append((i, j, 0))
                    visited_or_queued.add((i,j))

        minute_ans = bfs()
        
        if is_fully_rotten():
            return minute_ans

        return -1

        # O(m * n) - time
        # O(m * n) - space