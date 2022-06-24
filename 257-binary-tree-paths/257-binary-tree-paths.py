# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def getPath(root,ans,ans_string):
            if(root is None):
                return
            if(root.left is None and root.right is None):
                ans.append(ans_string+str(root.val))
            getPath(root.left,ans,ans_string+str(root.val)+"->")
            getPath(root.right,ans,ans_string+str(root.val)+"->")
        ans= []
        ans_string =""
        getPath(root,ans,ans_string)
        return ans