# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        link_list = list()
        curr = head
        while(curr):
            link_list.append(curr.val)
            curr = curr.next
        return link_list == link_list[::-1]