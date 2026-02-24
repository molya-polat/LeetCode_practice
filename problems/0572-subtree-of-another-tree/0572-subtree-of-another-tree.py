# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkSimilarity(node, sub_node):
            if not node and not sub_node:
                return True
            if not node or not sub_node or node.val != sub_node.val:
                return False
            
            left_similar = checkSimilarity(node.left, sub_node.left)
            right_similar = checkSimilarity(node.right, sub_node.right)
            return left_similar & right_similar

        
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                similar = checkSimilarity(node, subRoot)
                if similar:
                    return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        
        return False

# O(n * m) - time complexity, m - nodes or root, n - nodes of subroot
# O(m) - space complexity