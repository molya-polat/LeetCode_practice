from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()
        visited_or_queued = set()

        def is_valid(node):
            i, j = node

            return (0 <= i < n) and (0 <= j < m)


        def node2neighbours(node):
            i, j = node
            possible = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

            ans = []
            for ni, nj in possible:
                if is_valid((ni, nj)) and grid[ni][nj] == "1":
                    ans.append((ni, nj))
            
            return ans


        def dfs(node):
            visited.add(node)
            neighbours = node2neighbours(node)

            for to in neighbours:
                if to not in visited:
                    dfs(to)

        
        def bfs(node):
            queue = deque()
            
            queue.append(node)
            visited_or_queued.add(node)

            while len(queue) > 0:
                cur_node = queue.popleft()
                neighbours = node2neighbours(cur_node)

                for to in neighbours:
                    if to not in visited_or_queued:
                        queue.append(to)
                        visited_or_queued.add(to)

        
        number_of_islands = 0

        for i in range(n):
            for j in range(m):
                node = (i, j)

                if node not in visited_or_queued and grid[i][j] != '0':
                    bfs(node)
                    number_of_islands += 1

        return number_of_islands


        # Depth First Search
        # O(n * m) - Time complexity
        # O(n * m) - Memory complexity

        # Breadth First Search
        # O(n * m) - Time complexity
        # O(n * m) - Memory complexity