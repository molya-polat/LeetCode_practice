class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2 ** 31 - 1
        m = len(rooms)
        n = len(rooms[0])
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        def fill_neighbors(i, j, moves):
            possible_neighbors = [(i - 1, j), (i + 1, j), (i, j -1), (i, j + 1)]
            for ni, nj in possible_neighbors:
                if isValid(ni, nj) and rooms[ni][nj] != 0 and rooms[ni][nj] != -1 and rooms[ni][nj] > moves + 1:
                    rooms[ni][nj] = moves + 1
                    fill_neighbors(ni, nj, moves + 1)


        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    fill_neighbors(i, j, 0)

    # O(m * n) - time
    # O(1) - space