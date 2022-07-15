class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        big_val,small_val=nums[0],nums[-1]
        right_indx,left_indx=-1,-1
        for i in range(1,len(nums)):
            if(nums[i]>=big_val):
                big_val=nums[i]
            else:
                right_indx=i
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<=small_val):
                small_val=nums[i]
            else:
                left_indx=i
        
        if(left_indx<right_indx):
            return (right_indx-left_indx+1)
        else:
            return 0