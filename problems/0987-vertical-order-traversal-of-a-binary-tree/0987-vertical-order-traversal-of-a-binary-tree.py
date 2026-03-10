# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        diction = {}
        ans = []
        if not root:
            return [[]]
        def traverse(node, row, col):
            if node.left:
                traverse(node.left, row + 1, col - 1)
            if node.val not in diction:
                diction[node.val] = []
            diction[node.val].append((row, col))
            if node.right:
                traverse(node.right, row + 1, col + 1)

        traverse(root, 0, 0)
        column2values = {}
        for node_value, pairs in diction.items():
            for (row, col) in pairs:
                if col not in column2values:
                    column2values[col] = []
                column2values[col].append((row, node_value))

        sorted_keys = sorted(column2values.keys())

        for column in sorted_keys:
            sorted_row_values = sorted(column2values[column], key = lambda x: (x[0], x[1]))
            sorted_values = [x[1] for x in sorted_row_values]
            ans.append(sorted_values)
        
        return ans

        # O(nlpgn) - time
        # O(n) - space