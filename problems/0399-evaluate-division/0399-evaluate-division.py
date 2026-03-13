class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        diction = {}
        visited = set()
        for i in range(len(equations)):
            x, y = equations[i]
            if x not in diction:
                diction[x] = []
            diction[x].append((values[i], y))
            if y not in diction:
                diction[y] = []
            diction[y].append((1/values[i], x))
        
        def dfs(C, D):
            visited.add(C)
            if C not in diction:
                return -1
            if C == D:
                return 1
            neighbors = diction[C]
            for value, var in neighbors:
                if var not in visited:
                    result = dfs(var, D)
                    if result != -1:
                        return result * value
            
            return -1

        for C, D in queries:
            visited = set()
            result = dfs(C, D)
            ans.append(result)
        
        return ans
        # O(Q * E) - time, Q - queries, E - equations
        # O(V + E) - space, V - variables => O(E)