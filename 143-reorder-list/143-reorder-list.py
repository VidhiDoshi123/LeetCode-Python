# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        dummy=None
        while(curr):
            next_p=curr.next
            curr.next=dummy
            dummy=curr
            curr=next_p
        second=dummy
        first=head
        while(second):
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        
            