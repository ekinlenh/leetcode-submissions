# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode(-1)
        curr = new_head

        seen = set()
        while (head):
            if head.val not in seen:
                seen.add(head.val)
                curr.next = head
                curr = curr.next
            head = head.next
        
        curr.next = None
        return new_head.next
