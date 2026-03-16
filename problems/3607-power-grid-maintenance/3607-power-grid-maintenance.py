class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(c + 1)]
        # Time O(n)
        # Space O(n)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        diction = {}
        visited = set()
        grid = []
        def dfs(node, index):
            diction[node] = index
            visited.add(node)
            grid.append(node)

            for k in graph[node]:
                if k not in visited:
                    dfs(k, index)

        # Time O(c + n)
        # Space O(c)
        arr_st = []
        index = 0
        for i in range(1, c + 1):
            if i not in visited:
                grid = []
                dfs(i, index)
                heapq.heapify(grid)
                arr_st.append(grid)
                index += 1
        
        # O(c)
        active = set()
        for i in range(1, c + 1):
            active.add(i)

        # Time O(Q * log(c))
        # Space O(Q)
        ans = []
        for q, station in queries:
            if q == 2 and station in active:
                active.remove(station)
            elif q == 1:
                if station in active:
                    ans.append(station)
                else:
                    if station not in diction:
                        ans.append(-1)
                    else:
                        index = diction[station]
                        if len(arr_st[index]) > 0:
                            while arr_st[index] and arr_st[index][0] not in active:
                                s = heapq.heappop(arr_st[index])
                            if arr_st[index] and arr_st[index][0] in active:
                                s = arr_st[index][0]
                                ans.append(s)
                            else:
                                ans.append(-1)
                        else:
                            ans.append(-1)
            
        return ans

        # Time O(c + n + Q * log(c))
        # Space O(c + n + Q)