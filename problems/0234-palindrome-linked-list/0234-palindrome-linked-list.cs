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
    public bool IsPalindrome(ListNode head) {
        var pointer = head;
        var list = new List<int>();
        while(pointer != null){
            list.Add(pointer.val);
            pointer = pointer.next;
        }
        var length = list.Count;
        for (int i = 0; i < length / 2; i++){
            if (list[i] != list[length - i - 1]){
                return false;
            }
        }
        return true;
    }
}