# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # To remove in a singly linked list, you must keep track of the node previous of the removed node
        # So that we can set the prev_node.next -> removed_node->next to ensure connectivity 
        # This means we can use a two-pointers approach where we have a prev_node and a curr_node
        # To get the nth node from the end of the list, first we can traverse the linked list and get 
        # the size. Then we traverse again but until (size - n) and then remove curr_node
        # Test Case 1: [1] n = 1 -> size = 1, i in range(0, 0) -> return head.next which is null
        # Test Case 2: [1, 2] n = 1 -> size = 2, i in range(0, 1) -> prevNode = 1, currNode = 2, remove currNode

        # Get the size of the list
        # size = 0
        # currNode = head
        # while currNode:
        #     size += 1
        #     currNode = currNode.next
        
        # prevNode = None
        # currNode = head
        # for i in range(size - n): # Gets us to the nth node from the end of the list
        #     prevNode = currNode
        #     currNode = currNode.next
        
        # if not prevNode: # The node to remove is the first element in the list
        #     return head.next

        # prevNode.next = currNode.next
        # return head

        # Another approach: 
        # We can get a one-pass solution by using fast and slow pointers
        # Idea: Make fast pointer n nodes ahead of the slow pointer
        # This means when the fast pointer reaches the end, the slow pointer is the nth-1 node from the end of the list
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
 
        if not fast: # fast reached end before we can traverse (happens on size = 1)
            return head.next
        
        while fast.next: # We go until fast becomes null, which means slow is at nth-1 node from end of list
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head

