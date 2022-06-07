# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans =0
        def dfs_height(root):
            if(not root):
                return 0
            ldepth = dfs_height(root.left)
            rdepth = dfs_height(root.right)
            self.ans = max(self.ans,ldepth+rdepth)
            return 1 + max(ldepth,rdepth)
        dfs_height(root)
        return self.ans
        
        