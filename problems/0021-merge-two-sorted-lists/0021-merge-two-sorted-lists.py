# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        result_head = list1

        pointer1 = list1
        pointer2 = list2
        prev1 = None
        while pointer1 and pointer2:
            if pointer2.val < pointer1.val and prev1 == None or pointer2.val < pointer1.val and pointer2.val >= prev1.val:
                temp = pointer2.next
                pointer2.next = pointer1
                pointer1 = pointer2
                if prev1:
                    prev1.next = pointer2
                else:
                    result_head = pointer2
                
                pointer2 = temp
                
            elif pointer2.val >= pointer1.val and not pointer1.next or pointer2.val >= pointer1.val and pointer2.val < pointer1.next.val:
                temp2 = pointer2.next
                temp1 = pointer1.next
                pointer1.next = pointer2
                pointer1.next.next = temp1

                pointer2 = temp2
                if prev1:
                    prev1 = prev1.next
                else:
                    prev1 = pointer1
                pointer1 = pointer1.next
            else:
                if prev1:
                    prev1 = prev1.next
                else:
                    prev1 = pointer1
                pointer1 = pointer1.next
        
        return result_head

        # O(n) - time
        # O(1) - space