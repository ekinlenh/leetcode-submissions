# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # idea:
        # get the half-way mark of the palindrome
        # store each element in a stack
        # and traverse the right half of the list, checking with stack
        # if not equal, return False
        # need to differentiate between odd and even size

        size = 0
        curr = head
        while (curr):
            size += 1
            curr = curr.next
        
        if size == 0:
            return True

        stack = []
        curr = head
        idx = 0
        while (idx < (size // 2)):
            stack.append(curr.val)
            curr = curr.next
            idx += 1
        
        if (size % 2) == 1: # is odd
            curr = curr.next
        
        while (curr):
            val = stack.pop()
            if curr.val != val:
                return False
            curr = curr.next
        
        return True
