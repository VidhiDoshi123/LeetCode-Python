class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        cur_sum=0
        for i in range(0,len(nums)):
            cur_sum+=nums[i]
            if(cur_sum>maxi):
                maxi=cur_sum
            if(cur_sum<0):
                cur_sum=0
        return maxi