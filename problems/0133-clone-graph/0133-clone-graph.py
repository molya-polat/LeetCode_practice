"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        queue = deque()
        queue.append(node)
        diction = {}
        visited_or_queued = set()

        if not node:
            return

        while queue:
            node = queue.popleft()
            visited_or_queued.add(node.val)

            if node.val not in diction:
                new_node = Node(node.val)
                new_node.neighbors = []
                for n in node.neighbors:
                    if n.val not in diction:
                        new_neighbor = Node(n.val)
                        diction[n.val] = new_neighbor
                    else:
                        new_neighbor = diction[n.val]
                    new_node.neighbors.append(new_neighbor)
                    if n.val not in visited_or_queued:
                        queue.append(n)
                        visited_or_queued.add(n.val)
                diction[node.val] = new_node
            else:
                new_node = diction[node.val]
                if not new_node.neighbors:
                    new_node.neighbors = []
                for n in node.neighbors:
                    if n.val not in diction:
                        new_neighbor = Node(n.val)
                        diction[n.val] = new_neighbor
                    else:
                        new_neighbor = diction[n.val]
                    new_node.neighbors.append(new_neighbor)
                    if n.val not in visited_or_queued:
                        queue.append(n)
                        visited_or_queued.add(n.val)

        return diction[1]

# O(n) - time
# O(n) - space