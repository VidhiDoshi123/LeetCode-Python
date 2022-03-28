# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1=0
        n2 = 0
        if(headA == headB):
            return headA
        currA = headA
        currB = headB
        while(currA):
            n1+=1
            currA = currA.next
        while(currB):
            n2+=1
            currB = currB.next
        if(n1 > n2):
            diff = n1-n2
            for _ in range(0,diff):
                headA = headA.next
        elif(n2 > n1):
            diff = n2- n1
            for _ in range(0,diff):
                headB = headB.next
        if(headA == headB):
            return headA
        while(headA.next and headB.next):
            if(headA.next == headB.next):
                return headA.next
            headA = headA.next
            headB = headB.next
        if(headA.next is None or headB.next is None):
            return None