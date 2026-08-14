# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force: move to array then sort the array
        if not head:
            return
        if not head.next:
            return head

        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next

        res.sort()
        new_head = ListNode(res[0])
        curr = new_head
        i = 1
        while i < len(res):
            curr.next = ListNode(res[i])
            curr = curr.next
            i += 1
        
        return new_head


