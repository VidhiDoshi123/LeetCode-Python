# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        link_list = list()
        copy_list = list()
        while(temp):
            link_list.append(temp.val)
            temp = temp.next
        copy_list = [ x for x in link_list]
        start =0
        end = len(link_list)-1
        while(start<=end):
            link_list[start],link_list[end] = link_list[end],link_list[start]
            start+=1
            end-=1
        print(link_list,copy_list)
        return copy_list == link_list