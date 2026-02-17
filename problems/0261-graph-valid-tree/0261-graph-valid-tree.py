class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        visited = set()

        list_nodes = [[] for _ in range(n)]
        for a, b in edges:
            list_nodes[a].append(b)
            list_nodes[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            neighbors = list_nodes[node]
            for n in neighbors:
                dfs(n)
            
            return

        dfs(0)
        return len(visited) == n

# O(n) - time
# O(n) - space