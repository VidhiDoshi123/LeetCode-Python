# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(elements,root):
            if(root is None):
                return
            
            helper(elements,root.left)
            helper(elements,root.right)
            elements.append(root.val)
        elements=[]
        helper(elements,root)
        return elements