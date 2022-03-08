class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        present_sum = 0
        max_sum = -99999999999999999999999999999999
        for i in range(0,len(nums)):
            present_sum = present_sum + nums[i]
            if( present_sum > max_sum):
                max_sum = present_sum
            if( present_sum < 0 ):
                present_sum = 0
        return max_sum
                