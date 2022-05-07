class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        nums.sort()
        start = 0
        end = len(nums)-1
        for i in range(len(nums)):
            if(nums[i] ==target):
                ans.append(i)
        return ans
            