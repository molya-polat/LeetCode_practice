# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        current_level = 0
        node = root
        
        def dfs(node, level):
            if not node:
                return None
            if level == len(ans):
                ans.append(node.val)
            
            if node.right:
                dfs(node.right, level + 1)
            
            if node.left:
                dfs(node.left, level + 1)
        
        dfs(root, 0)
        return ans

        # O(n) - time
        # O(n) - space