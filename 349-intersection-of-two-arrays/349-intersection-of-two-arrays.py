class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = list()
        def bse(target,nums,start,end):
            while(start<=end):
                mid = (start+end)//2
                if(nums[mid]==target):
                    return True
                elif(nums[mid]>target):
                    end = mid-1
                else:
                    start= mid+1
            return False
            
        for num in nums1:
            if(bse(num,nums2,0,len(nums2)-1)):
                if(num not in ans):
                    ans.append(num)
        return ans
                
            