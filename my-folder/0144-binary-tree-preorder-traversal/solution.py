# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        # res = []
        # def dfs(root):
        #     if root is None:
        #         return
            
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # return res

        res = []

        if not root:
            return res

        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res

