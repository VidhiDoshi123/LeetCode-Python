# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance=True
        def height(root):
            if(root is None):
                return 0
            ldepth=height(root.left)
            rdepth = height(root.right)
            if(abs(ldepth-rdepth)>1):
                self.balance=False
            return max(ldepth,rdepth)+1
        height(root)
        return self.balance
        