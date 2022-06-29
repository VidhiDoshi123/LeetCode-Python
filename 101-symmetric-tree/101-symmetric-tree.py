# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymmetricHelper(left,right):
            if(left is None or right is None):
                return left==right
            if(left.val!=right.val):
                return False
            return (isSymmetricHelper(left.left,right.right) and isSymmetricHelper(left.right,right.left))
        if(root is None):
            return False
        return isSymmetricHelper(root.left,root.right)
        
        