/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        int sizeA = 0, sizeB = 0;

        while (a != null) {
            sizeA++;
            a = a.next;
        }

        while (b != null) {
            sizeB++;
            b = b.next;
        }

        int diff = Math.abs(sizeA - sizeB);
        a = headA;
        b = headB;

        if (sizeA > sizeB) {
            while (diff != 0) {
                diff--;
                a = a.next;
            }
        } else {
            while (diff != 0) {
                diff--;
                b = b.next;
            }
        }

        while (a != null && b != null) {
            if (a == b) {
                return a;
            }
            a = a.next;
            b = b.next;
        }

        return null;
    }
}
