# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == 1:
            return None
        mid = length // 2
        node = head
        prev = None
        i = 0
        while True:
            if i == mid and prev:
                prev.next = node.next
                break
            i += 1
            prev = node
            node = node.next

        return head
        # O(n) - time
        # O(1) - space