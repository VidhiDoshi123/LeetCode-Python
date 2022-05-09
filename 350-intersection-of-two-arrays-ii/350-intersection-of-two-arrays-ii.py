class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ptr1= 0
        ptr2 = 0
        nums1.sort()
        nums2.sort()
        ans = list()
        while(ptr1<=(len(nums1)-1) and ptr2 <= (len(nums2)-1)):
            if(nums1[ptr1]<nums2[ptr2]):
                ptr1+=1
            elif(nums1[ptr1]>nums2[ptr2]):
                ptr2+=1
            else:
                ans.append(nums1[ptr1])
                ptr1+=1
                ptr2+=1
        return ans