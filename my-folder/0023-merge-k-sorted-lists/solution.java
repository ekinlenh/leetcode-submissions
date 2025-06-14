/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // we can also implement the merge sort of two linked lists into this problem
        // Time Complexity: O(n * k)
        // Space Complexity: O(1)

        if (lists.length == 0) {
            return null;
        }

        for (int i = 1; i < lists.length; i++) {
            lists[i] = mergeTwoLists(lists[i], lists[i - 1]);
        }

        // last element of lists[] will have fully merged and sorted linked list
        return lists[lists.length - 1];
    }

    // from previous leetcode problem
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(-1);
        ListNode current = temp;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }

            current = current.next;
        }

        if (l1 != null) {
            current.next = l1;
        } else {
            current.next = l2;
        }

        return temp.next;
    }
}
