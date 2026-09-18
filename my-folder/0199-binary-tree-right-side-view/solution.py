# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # right side view means that 
        # the last node in every level is the node viewed from the right
        # therefore we can perform BFS on the tree, and only append the last node of each level
        # this gives us the right side view

        res = []

        if root is None:
            return res

        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    res.append(node.val)

        return res
