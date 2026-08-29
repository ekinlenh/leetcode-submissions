# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # traverse head to left while keeping track of the nodes in this left portion
        dummy = ListNode(-1)
        dummy.next = head
        
        before = dummy
        curr = head
        for _ in range(left - 1):
            before = before.next
            curr = curr.next

        # now curr should be at left, so we can start reversing
        prev = None
        left_node = curr
        while curr and left <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left += 1

        # get the right side of the list (which is at curr)
        left_node.next = curr

        # set before.next to start of the reversed list
        before.next = prev

        return dummy.next

