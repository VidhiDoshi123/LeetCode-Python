class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for num in nums1:
            index = nums2.index(num)
            flag = False
            for j in range(index,len(nums2)):
                if(nums2[j]> num):
                    flag= True
                    ans.append(nums2[j])
                    break
            if(not flag):
                ans.append(-1)
        return ans
                    