# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        queue = deque()
        diction = {}
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val not in diction:
                diction[node.val] = []
            
            if node.left:
                queue.append(node.left)
                diction[node.val].append(node.left.val)
                diction[node.left.val] = [node.val]
            if node.right:
                queue.append(node.right)
                diction[node.val].append(node.right.val)
                diction[node.right.val] = [node.val]
        minutes = 0
        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        while queue:
            node, minute = queue.popleft()
            adj = diction[node]
            for a in adj:
                if a not in visited:
                    queue.append((a, minute + 1))
                    visited.add(a)
            
            minutes = minute
        
        return minutes
        # O(n) - time
        # O(n) - space