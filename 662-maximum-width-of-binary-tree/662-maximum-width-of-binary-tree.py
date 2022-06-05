# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q= collections.deque()
        res = 0
        q.append((root,0))
        while(q):
            _lnode,lpos = q[0]
            _rnode,rpos = q[-1]
            res= max(res,rpos-lpos+1)
            qlen= len(q)
            for _ in range(qlen):
                node,pos= q.popleft()
                if(node.left):
                    q.append((node.left,2*pos+1))
                if(node.right):
                    q.append((node.right,2*pos+2))
        return res