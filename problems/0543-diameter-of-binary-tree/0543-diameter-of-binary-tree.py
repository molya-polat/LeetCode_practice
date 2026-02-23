# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        def level(node):
            nonlocal max_length
            left_level, right_level = 0, 0
            if node.left:
                left_level = level(node.left) + 1
            if node.right:
                right_level = level(node.right) + 1
            max_length = max(max_length, left_level + right_level)
            if node.left and node.right: 
                return max(left_level, right_level)

            if node.left:
                return left_level
            
            if node.right:
                return right_level
            
            return 0
        
        result = level(root)
        return max_length

        # O(n) - time
        # O(1) - space