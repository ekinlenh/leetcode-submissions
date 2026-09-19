# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_val):
            if root is None:
                return 0
            
            good = 1 if root.val >= max_val else 0 

            max_val = max(max_val, root.val)
            return good + dfs(root.left, max_val) + dfs(root.right, max_val)

        return dfs(root, float('-inf'))

