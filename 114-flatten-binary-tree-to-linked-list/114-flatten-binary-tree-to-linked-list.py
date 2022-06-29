# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root is None):
            return root
        elements=[]
        def preorder(root,elements):
            if(root is None):
                return
            elements.append(root)
            preorder(root.left,elements)
            preorder(root.right,elements)
        preorder(root,elements)
        print(elements)
        root = elements.pop(0)
        root.left = None
        temp = root
        while(elements):
            node = elements.pop(0)
            node.left= None
            temp.right= node
            temp= temp.right
        return root