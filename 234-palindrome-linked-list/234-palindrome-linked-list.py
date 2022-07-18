# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = None
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            slow= slow.next
            fast= fast.next.next
        curr= slow.next
        while(curr is not None):
            next_pointer=curr.next
            curr.next=dummy
            dummy= curr
            curr=next_pointer
        slow.next=dummy
        slow=head
        while(dummy is not None):
            if(slow.val != dummy.val):
                return False
            slow=slow.next
            dummy=dummy.next
        return True
        