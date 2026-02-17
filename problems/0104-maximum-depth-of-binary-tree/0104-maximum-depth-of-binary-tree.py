# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxDp(node):
            leftDp = 1
            rightDp = 1
            if not node.left and not node.right:
                return 1
            if node.left:
                leftDp = maxDp(node.left) + 1
            if node.right:
                rightDp = maxDp(node.right) + 1
            return max(leftDp, rightDp)
        
        return maxDp(root)

        # O(n) - time
        # O(1) - space