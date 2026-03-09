from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start_node = "0000"
        if start_node == target:
            return 0
        de_st = set(deadends)

        visited = set()

        def isNotDeadEnd(code):
            return code not in de_st
        
        if not isNotDeadEnd(start_node):
            return -1
        
        def getAllPossibleValidNeighbors(node):
            ans = []
            for i in range(len(node)):
                ch_int = int(node[i])
                prev_digit = (ch_int - 1) % 10
                next_digit = (ch_int + 1) % 10
                neighbor = node[:i] + str(prev_digit) + node[i + 1:]
                if isNotDeadEnd(neighbor):
                    ans.append(neighbor)
                neighbor = node[:i] + str(next_digit) + node[i + 1:]
                if isNotDeadEnd(neighbor):
                    ans.append(neighbor)

            return ans

        queue = deque()
        queue.append((start_node, 0))
        visited.add(start_node)

        
        while queue:
            c_node, move = queue.popleft()
            neighbors = getAllPossibleValidNeighbors(c_node)
            for neighbor in neighbors:
                if neighbor == target:
                    return move + 1
                if neighbor not in visited:
                    queue.append((neighbor, move + 1))
                    visited.add(neighbor)
            
        return -1