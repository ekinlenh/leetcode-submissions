# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # we need to keep track of a prev node (where prev.next is reassigned to swapped node)
        # reverse the two adjacent nodes

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        first = head
        second = head.next
        while first and first.next:
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            first = first.next

        return dummy.next
