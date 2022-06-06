# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        q = deque([root])
        ans = []
        while(q):
            
            level_array = []
            qLen = len(q)
            for i in range(qLen):
                popedNode = q.popleft()
                level_array.append(popedNode.val)
                if(popedNode.left):
                    q.append(popedNode.left)
                if(popedNode.right):
                    q.append(popedNode.right)
            ans.append(level_array)
        return ans
                