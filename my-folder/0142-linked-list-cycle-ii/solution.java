/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // we can use a fast and slow pointer
        // which will meet if there is a cycle in the linked list

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if(fast==slow) {
                ListNode slow2 = head;
                while(slow != slow2){
                    slow=slow.next;
                    slow2=slow2.next;
                }
            return slow2;
            }
        }

        return null;
    }
}
