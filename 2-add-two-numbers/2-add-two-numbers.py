# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        start = dummy
        while l1 and l2:
            digit_sum = l1.val + l2.val
            if(carry==1):
                digit_sum+=1
            if(digit_sum > 9):
                carry = 1
            else: 
                carry =0
            new_node = ListNode(digit_sum%10)
            dummy.next= new_node
            dummy = new_node
            l1 = l1.next
            l2 = l2.next
        while(l1):
            digit_sum = l1.val + carry
            if(digit_sum > 9):
                carry = 1
            else:
                carry = 0
            new_node = ListNode(digit_sum%10)
            dummy.next = new_node
            dummy = new_node
            l1 = l1.next
        while(l2):
            digit_sum = l2.val + carry
            if(digit_sum > 9):
                carry = 1
            else:
                carry = 0
            new_node = ListNode(digit_sum%10)
            dummy.next = new_node
            dummy = new_node
            l2 = l2.next
        if(carry ==1):
            new_node = ListNode(1)
            dummy.next = new_node
            dummy = new_node
        return start.next
            