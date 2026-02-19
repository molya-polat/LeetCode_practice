# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        condList = []
        def isValid(node, conditionsList):
            if conditionsList:
                for more, value in conditionsList:
                    if (more and node.val <= value) or (not more and node.val >= value):
                        return False

            ans1, ans2 = True, True
            if not conditionsList:
                conditionsList = []
            if node.left:
                shouldBeMore = False
                leftConditionList = conditionsList[:]
                leftConditionList.append((shouldBeMore, node.val))
                ans1 = isValid(node.left, leftConditionList)
            if node.right:
                shouldBeMore = True
                rightConditionList = conditionsList[:]
                rightConditionList.append((shouldBeMore, node.val))
                ans2 = isValid(node.right, rightConditionList)

            return ans1 & ans2
        
        return isValid(root, condList)

# O(n) - time
# O(n^2) - space