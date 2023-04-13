/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle(ListNode head) {
        if (head == null) return false;
        var current = head;
        var hashset = new HashSet<ListNode>();
        while (current != null){
            if (!hashset.Contains(current)){
                hashset.Add(current);
                current = current.next;
            }
            else{
                return true;
            }
        }
        return false;
    }
}