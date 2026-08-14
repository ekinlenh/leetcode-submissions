# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # idea: make two lists: one < x ; one >= x
        # then we can connect these two lists together 

        l = ListNode() # less than list
        geq = ListNode() # greater than or equal to list

        l_curr = l
        geq_curr = geq

        while head:
            if head.val < x:
                l_curr.next = head
                l_curr = l_curr.next
            else:
                geq_curr.next = head
                geq_curr = geq_curr.next
            
            head = head.next
        
        l_curr.next = geq.next
        geq_curr.next = None

        return l.next
        
        
