# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # plan: traverse inorder with an array, then return the kth - 1 element

        res = []
        def inorder(root, res):
            if root is None:
                return
            
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        
        inorder(root, res)
        return res[k - 1]
