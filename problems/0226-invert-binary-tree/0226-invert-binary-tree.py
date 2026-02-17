# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        def invert(node):
            if not node.left and not node.right:
                return node
            
            if node.left and node.right:
                invert(node.left)
                invert(node.right)
                temp = node.right
                node.right = node.left
                node.left = temp
            elif node.left and not node.right:
                invert(node.left)
                node.right = node.left
                node.left = None
            else:
                invert(node.right)
                node.left = node.right
                node.right = None
            
            return node

        root = invert(root)
        return root

        # O(n) - time
        # O(1) - space