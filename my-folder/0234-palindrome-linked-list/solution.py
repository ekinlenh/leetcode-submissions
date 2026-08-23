# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # last solution using stack was time O(n) and space O(n)
        # we can make this time O(n) and O(1) space using fast/slow pointers
        # slow pointer will be at middle point of the list
        # then we can reverse the first half of the list
        # and traverse normally with slow pointer until end and see if values are equal
        if not head or not head.next:
            return True
                
        slow, fast = head, head

        # find middle while reversing first half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:  # is odd
            slow = slow.next
        
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True
