class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        diction = {}
        visited = set()

        def dfs(node, a):
            if node not in diction:
                return False
            visited.add(node)
            for neighbor in diction[node]:
                if neighbor == a:
                    return True
                
                if neighbor not in visited:
                    ans = dfs(neighbor, a)
                    if ans:
                        return True
            
            return False


        for a, b in edges:
            visited = set()
            isRedundant = dfs(b, a)
            if isRedundant:
                return [a, b]
            if a not in diction:
                diction[a] = {b}
            else:
                diction[a].add(b)
            if b not in diction:
                diction[b] = {a}
            else:
                diction[b].add(a)
        
        return []

        # O(n^2) - time
        # O(n) - space








        # adj_list = [[] for _ in range(n + 1)]
        # for a, b in edges:
        #     adj_list[a].append(b)
        #     adj_list[b].append(a)
        
        # visited_nodes = set()
        # visited_edges = set()

        # def dfs(node):
        #     visited_nodes.add(node)
        #     for neighbor in adj_list[node]:
        #         if neighbor in visited_nodes and (node,neighbor) not in visited_edges:
        #             return (neighbor, node)
        #         elif neighbor not in visited_nodes:
        #             visited_edges.add((node, neighbor))
        #             visited_edges.add((neighbor, node))
        #             result = dfs(neighbor)
        #             return result


        # return dfs(1)


        # # O(n) - time complexity; n - nodes, m - edges (m = n - 1)
        # # O(n) - space complexity