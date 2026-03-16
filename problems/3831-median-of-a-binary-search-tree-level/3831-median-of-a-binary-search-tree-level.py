# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:
        arr = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, l = queue.popleft()
            if l == level:
                arr.append(node.val)
            if node.left:
                queue.append((node.left, l + 1))
            
            if node.right:
                queue.append((node.right, l + 1))
        if not arr:
            return -1
        return arr[len(arr) // 2]

        # O(n) - time
        # O(2^level) - space