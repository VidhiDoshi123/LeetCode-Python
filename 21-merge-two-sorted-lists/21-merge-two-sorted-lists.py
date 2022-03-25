# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        result = dummy
        pointer1 = list1
        pointer2 = list2
        while(pointer1 and pointer2):
            if(pointer1.val <= pointer2.val):
                dummy.next = pointer1
                pointer1 = pointer1.next
            else:
                dummy.next = pointer2
                pointer2 = pointer2.next
            dummy = dummy.next
        if(pointer1):
            dummy.next = pointer1
        elif(pointer2):
            dummy.next = pointer2 
        return result.next
            
                