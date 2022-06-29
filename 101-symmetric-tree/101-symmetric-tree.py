# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q=[(root.left,root.right)]
        while(q):
            left_subtree,right_subtree = q.pop()
            if(left_subtree is None and right_subtree is None):
                continue
            if((left_subtree is not None and right_subtree is None) or(left_subtree is None and right_subtree is not None) or left_subtree.val!=right_subtree.val):
                return False
            q.append((left_subtree.left,right_subtree.right))
            q.append((left_subtree.right,right_subtree.left))
        return True
        
        