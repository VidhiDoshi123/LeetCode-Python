# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        dummy = None
        curr = head
        while(curr):
            next_pointer = curr.next
            curr.next = dummy
            dummy = curr
            curr = next_pointer
        return dummy
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse(slow.next)
        slow = slow.next
        start = head
        while(slow):
            if(slow.val != start.val):
                return False
            slow = slow.next
            start = start.next
        return True