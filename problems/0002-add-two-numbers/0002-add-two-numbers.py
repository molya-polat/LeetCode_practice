# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        power = 0
        while l1:
            number1 = number1 + l1.val * 10**power
            l1 = l1.next
            power += 1
    
        number2 = 0
        power = 0
        while l2:
            number2 = number2 + l2.val * 10**power
            l2 = l2.next
            power += 1

        result = number1 + number2
        result_node = ListNode()
        result_node.val = result % 10
        temp = result_node
        result = result // 10
        while result > 0:
            new_node = ListNode()
            remainder = result % 10
            new_node.val = remainder
            temp.next = new_node
            result = result // 10
            temp = new_node
        
        return result_node

        # O(n) - time
        # O(1) - space