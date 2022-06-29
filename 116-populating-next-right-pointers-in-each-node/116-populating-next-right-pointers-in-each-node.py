"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=[root]
        while(q):
            qlen= len(q)
            for i in range(0,qlen):
                node= q.pop(0)
                if(i<(qlen-1)):
                    node.next=q[0]
                if(node and node.left):
                    q.append(node.left)
                if(node and node.right):
                    q.append(node.right)
        return root
            
        