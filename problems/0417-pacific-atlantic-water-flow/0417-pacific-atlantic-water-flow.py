class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        ans = []
        visited_pacific = set()
        visited_atlantic = set()


        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs_pacific(i, j):
            visited_pacific.add((i, j))
            possible = [(i - 1, j), (i + 1, j), (i , j - 1), (i, j + 1)]
            for ni, nj in possible:
                if isValid(ni, nj) and heights[ni][nj] >= heights[i][j] and (ni, nj) not in visited_pacific:
                    dfs_pacific(ni, nj)


        
        def dfs_atlantic(i, j):
            visited_atlantic.add((i, j))
            possible = [(i - 1, j), (i + 1, j), (i , j - 1), (i, j + 1)]
            for ni, nj in possible:
                if isValid(ni, nj) and heights[ni][nj] >= heights[i][j] and (ni, nj) not in visited_atlantic:
                    dfs_atlantic(ni, nj)
            


        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs_pacific(i, j)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dfs_atlantic(i, j)
        
        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in visited_pacific and (i, j) in visited_atlantic:
        #             ans.append([i, j])
        
        return list(visited_pacific & visited_atlantic)

        # O(m * n) - time
        # O(m * n) - space
























        # visited = set()
        # memo = {}
        # def isValid(i, j):
        #     return 0 <= i < m and 0 <= j < n

        # def dfs_pacific(i, j):
                

        # def dfs(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if (i, j) not in visited:
        #         visited.add((i, j))
        #     pac, atl = 0, 0
        #     if i == 0 or j == 0:
        #         pac = 1
        #     if i == m - 1 or j == n - 1:
        #         atl = 1

        #     possible = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        #     for ni, nj in possible:
        #         if isValid(ni, nj) and heights[ni][nj] == heights[i][j] and (ni, nj) in visited and (ni, nj) in memo:
        #             pacific, atlantic = memo[(ni, nj)]
        #             if pacific == 1:
        #                 pac = 1
        #             if atlantic == 1:
        #                 atl = 1
        #         if isValid(ni, nj) and ((heights[ni][nj] < heights[i][j]) or (heights[ni][nj] == heights[i][j] and (ni, nj) not in visited)):
        #             pacific, atlantic = dfs(ni, nj)
        #             if pacific == 1:
        #                 pac = 1
        #             if atlantic == 1:
        #                 atl = 1
        #     if pac == 1 and atl == 1:
        #         ans.append([i, j])
        #     memo[(i, j)] = (pac, atl)
        #     return (pac, atl)
        

        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) not in visited and (i, j) not in memo:
        #             pac, atl = dfs(i, j)
        
        # return ans



            
        











        # pacific = [[0] * n for _ in range(m)]
        # atlantic = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0:
        #             pacific[i][j] = 1
        #             continue
        #         if j == 0:
        #             pacific[i][j] = 1
        #             continue
        #         if (heights[i - 1][j] <= heights[i][j] and pacific[i - 1][j] == 1) or (heights[i][j - 1] <= heights[i][j] and pacific[i][j - 1] == 1):
        #             pacific[i][j] = 1
        
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if i == m - 1:
        #             atlantic[i][j] = 1
        #             continue
        #         if j == n - 1:
        #             atlantic[i][j] = 1
        #             continue
                
        #         if (heights[i + 1][j] <= heights[i][j] and atlantic[i + 1][j] == 1) or (heights[i][j + 1] <= heights[i][j] and atlantic[i][j + 1] == 1) :
        #             atlantic[i][j] = 1
                
        #         if (heights[i + 1][j] <= heights[i][j] and pacific[i + 1][j] == 1) or (heights[i][j + 1] <= heights[i][j] and pacific[i][j + 1] == 1) :
        #             pacific[i][j] = 1
                

                
        # print(pacific)
        # print(atlantic)
        # for i in range(m):
        #     for j in range(n):
        #         if pacific[i][j] == 1 and atlantic[i][j] == 1:
        #             ans.append([i, j])

        # return ans