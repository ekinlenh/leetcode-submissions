# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        
        def dfs(root):
            if root is None: 
                return 0
            
            # i want the max length of the left subtree and right subtree from a certain root node
            # the diameter of the tree is the sum of these two lengths
            # then, keep track of the max diameter we have seen
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal max_length
            max_length = max(max_length, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return max_length
