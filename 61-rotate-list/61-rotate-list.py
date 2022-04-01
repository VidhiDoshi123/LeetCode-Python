# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        curr = head
        length = 0
        while(curr):
            length+=1
            curr = curr.next
        if(k == length or k%length == 0):
            return head
        counter = length - (k%length)
        count = 1
        temp = head
        next_pointer = temp.next
        while(count!=counter):
            count+=1
            temp = temp.next
            next_pointer = temp.next
        temp.next = None
        new_head = next_pointer
        print(next_pointer,new_head)
        while(next_pointer.next):
            next_pointer = next_pointer.next
        next_pointer.next = head
        return new_head
        
        