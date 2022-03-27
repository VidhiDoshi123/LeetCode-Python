# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = 0
        curr = head
        prev = head
        temp = head
        if(head.next is None):
            return None
        while(curr):
            nodes+=1
            curr = curr.next
        prev_node = nodes - n
        print(prev_node)
        i = 0
        if(i==0 and prev_node==0):
            head = head.next
        while(i<prev_node):
            i = i+ 1
            temp = prev
            prev = prev.next
        print(i,temp.val,prev.val)
        temp.next = prev.next
        return head