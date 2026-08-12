# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # idea: keep two pointers (slow and fast)
        # make fast pointer k places ahead, which will make slow stop at k before the end once fast reaches end
        # then we store slow.next. this makes us have [slow.next, fast] which is the k rotations we need to move
        # to the front of the list
        # then we connect [slow.next, fast] to [head, slow]
        # edge case in example 2: if k > size of list, we can do k % size == 1
        # so first we need to grab the size of the linked list as well

        if head == None: # if list is empty
            return

        if head.next == None: # only one element in the list
            return head

        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        size = k % size # to prevent k > len(list)

        if size == 0: # do nothing
            return head

        slow = head
        fast = head
        for i in range(size):
            fast = fast.next

        while fast.next: # stops when fast is last node in the list
            slow = slow.next
            fast = fast.next

        new_head = slow.next # section off the part that needs to go to the front
        slow.next = None # slow.next will become the new tail node

        fast.next = head # make the tail node = head node of old list
        return new_head # return new_head [new_head, slow] is the new list

