class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        dp = nums
        for i in range(1,len(nums)):
            dp[i] = max(dp[i], nums[i] + dp[i-1])
        return max(dp)