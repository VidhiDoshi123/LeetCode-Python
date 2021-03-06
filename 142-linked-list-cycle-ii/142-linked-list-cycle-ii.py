# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        is_cycle=False
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                is_cycle=True
                break
        
        if(is_cycle):
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            if(slow==fast):
                return slow
        
        if(not is_cycle):
            return None