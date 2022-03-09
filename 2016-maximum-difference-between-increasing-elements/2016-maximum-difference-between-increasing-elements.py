class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_right = 99999999999999999999999999
        for i in range(len(nums)):
            if(min_right >= nums[i]):
                min_right = nums[i]
            else:
                max_diff = max(max_diff,nums[i] - min_right)
        return max_diff