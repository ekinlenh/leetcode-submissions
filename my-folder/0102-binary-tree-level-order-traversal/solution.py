# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # use bfs

        res = []

        queue = deque()
        queue.append(root)

        while queue:

            l = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

                    l.append(node.val)
            
            if l:
                res.append(l)
        
        return res
