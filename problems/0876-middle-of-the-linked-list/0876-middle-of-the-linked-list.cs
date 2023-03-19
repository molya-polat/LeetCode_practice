/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        int counter = 1;
        var pointer = new ListNode (head.val, head.next);
        while (pointer.next !=  null){            
            counter++;
            pointer = pointer.next;
        }
        int current = 1;
        counter = counter / 2 + 1;     
          while (head.next !=  null){
           if (current == counter){
                return head;
           }
            head = head.next;
            current++;
        }
        return head;
    }
}