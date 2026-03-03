# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = 0
        node = head
        result = head
        prev = None
        while node.next:
            temp = node
            if node.val == node.next.val:
                node = node.next
                if prev:
                    prev.next = node
                temp.next = None
                if start == 0:
                    result = node
            else:
                prev = node
                node = node.next
                start += 1
        
        return result

        # O(n)- time
        # O(1) - space