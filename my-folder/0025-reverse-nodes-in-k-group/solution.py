# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        first = None
        second = head
        for _ in range(size // k):
            first = None
            group_start = second

            i = 0
            while second and i < k:
                temp = second.next
                second.next = first
                first = second
                second = temp
                i += 1

            # connect previous to reversed group
            prev.next = first
            # group start is the tail of the reversed group
            group_start.next = second
            # move prev to tail for next group
            prev = group_start
        
        return dummy.next
            
