# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        memo = {}
        def possible_sums(node):
            if node not in memo:
                sums = [node.val]
                left_child_sums = []
                right_child_sums = []
                if node.left:
                    left_child_sums = possible_sums(node.left)
                if node.right:
                    right_child_sums = possible_sums(node.right)
                for lsm in left_child_sums:
                    sums.append(lsm + node.val)
                for rsm in right_child_sums:
                    sums.append(rsm + node.val)
                memo[node] = sums
            
            return memo[node]



        def check(node):
            current_sum = node.val
            paths = 0
            if current_sum == targetSum:
                paths += 1
            if node.left:
                possible_sums_left = possible_sums(node.left)
                for sm in possible_sums_left:
                    if sm + current_sum == targetSum:
                        paths += 1
            if node.right:
                possible_sums_right = possible_sums(node.right)
                for sm in possible_sums_right:
                    if sm + current_sum == targetSum:
                        paths += 1
            
            if node.left:
                paths += check(node.left)
            if node.right:
                paths += check(node.right)
            
            return paths
            


        paths_result = check(root)

        return paths_result