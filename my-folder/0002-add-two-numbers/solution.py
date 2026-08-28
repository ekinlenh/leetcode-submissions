# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # idea:
        # reverse l1 and l2
        # because we want to start from the one's place
        # then, we can add the digits in l1.val and l2.val current
        # if this current val >= 10, we need to have a carry over and set the curr val to be the remainder
        # ex: [2, 4, 3], [5, 6, 4] -> [3, 4, 2], [4, 6, 5]
        # 3 + 4 = 7, 4 + 6 = 10 % 10 = 0, 2 + 5 + (carry_over = 1) = 8
        # another ex: [1, 2, 3], [4, 5, 6] -> [3, 2, 1], [6, 5, 4] ; expected: 579 [9, 7, 5]
        # 3 + 6 = 9, 2 + 5 = 7, 1 + 4 = 5 -> [9. 7, 5]
        # misread problem, we don't reverse
        # bad examples honestly

        # go through both lists until one is null
        carry_over = 0
        head = ListNode(-1)

        curr = head
        while l1 and l2:
            res = l1.val + l2.val + carry_over
            if res >= 10:
                res = res % 10
                carry_over = 1
            else:
                carry_over = 0
            
            curr.next = ListNode(res)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next
        
        # there can still be leftover nodes to calculate
        while l1:
            res = l1.val + carry_over
            if res >= 10:
                res = res % 10
                carry_over = 1
            else:
                carry_over = 0

            curr.next = ListNode(res)
            curr = curr.next

            l1 = l1.next
        
        while l2:
            res = l2.val + carry_over
            if res >= 10:
                res = res % 10
                carry_over = 1
            else:
                carry_over = 0

            curr.next = ListNode(res)
            curr = curr.next

            l2 = l2.next

        if carry_over != 0:
            curr.next = ListNode(carry_over)

        return head.next
