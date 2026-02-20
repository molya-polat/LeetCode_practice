# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        sorted_list = []
        def f(node):
            if not node:
                return
            f(node.left)
            sorted_list.append((node.val, node))
            f(node.right)

        f(root)
        # print([a for a, _ in sorted_list])
        first_mistake_node, second_mistake_node = None, None
        for i in range(1, len(sorted_list)):
            (prev_val, prev_node) = sorted_list[i - 1]
            (val, node) = sorted_list[i]
            # print('index', i, 'value', val)
            if prev_val > val:
                if not first_mistake_node:
                    first_mistake_node = prev_node
                    second_mistake_node = node
                else:
                    # print("HIIIII")
                    second_mistake_node = node
                    break
        #     if first_mistake_node:
        #         print(first_mistake_node.val)
        #     if second_mistake_node:
        #         print(second_mistake_node.val)
        
        # if first_mistake_node:
        #     print(first_mistake_node.val)
        # if second_mistake_node:
        #     print(second_mistake_node.val)
        
        temp = first_mistake_node.val
        # print(second_mistake_node)
        first_mistake_node.val = second_mistake_node.val
        second_mistake_node.val = temp


        






























        # def find_second_and_swap(first_node, value):
        #     queue = deque()
        #     queue.append(root)
        #     while queue:
        #         second = queue.popleft()
        #         if second.val == value:
        #             temp = first_node.val
        #             first_node.val = second.val
        #             second.val = temp
        #         else:
        #             queue.append(second.left)
        #             queue.append(second.right)


        # def checkValidity(node, low, high):
        #     if node.val >= low and node.val <= high:
        #         if node.left:
        #             checkValidity(node.left, low, node.val)
        #         if node.right:
        #             checkValidity(node.right, node.val, high)
                
        #     elif node.val < low and node.val <= high:
        #         find_second_and_swap(node, low)
        #     elif node.val > high and node.val >= low:
        #         find_second_and_swap(node, high)
            
        
        # checkValidity(root, - 2**31, 2**31 - 1)