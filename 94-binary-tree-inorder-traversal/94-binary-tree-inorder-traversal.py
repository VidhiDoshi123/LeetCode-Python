# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,elements):
            if(root is None):
                return
            helper(root.left,elements)
            elements.append(root.val)
            helper(root.right,elements)
            
        elements =[]
        helper(root,elements)
        return elements