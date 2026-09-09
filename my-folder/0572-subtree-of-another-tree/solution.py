# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to first find when root.val == subRoot.val
        # and then we compare if these are the same trees
        def sameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            
            if (root and not subRoot) or (not root and subRoot):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        if root is None:
            return False
        
        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

