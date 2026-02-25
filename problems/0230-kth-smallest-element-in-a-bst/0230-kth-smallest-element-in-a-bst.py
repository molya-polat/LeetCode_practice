# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numbers_sorted = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            
            numbers_sorted.append(node.val)

            if node.right:
                traverse(node.right)
        
        traverse(root)   
        return numbers_sorted[k - 1]

        # O(n) - time
        # O(n) - space