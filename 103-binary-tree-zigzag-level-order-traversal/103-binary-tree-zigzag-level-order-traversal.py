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
        while(q):
            level =[]
            qlen = len(q)
            for _ in range(qlen):
                node = q.pop(0)
                if(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(len(level)!=0):
                ans.append(level)
        for i in range(len(ans)):
            if(i%2!=0):
                odd_level = ans.pop(i)
                reverse_odd_level = odd_level[::-1]
                ans.insert(i,reverse_odd_level)
        return ans
        