# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        ans =[]
        q.append(root)
        change = False
        while(q):
            level =[]
            qlen = len(q)
            for _ in range(qlen):
                node = q.pop(0)
                if(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(len(level)!=0 and not change):
                ans.append(level)
            elif(len(level)!=0 and change):
                ans.append(level[::-1])
            change = not change
                
        
        return ans
        