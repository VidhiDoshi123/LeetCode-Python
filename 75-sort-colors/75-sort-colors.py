class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = nums.count(0)
        count1 = nums.count(1)
        count2 = nums.count(2)
        for i in range(0,count0):
            nums[i] = 0
        for i in range(count0,count0+count1):
            nums[i] = 1
        for i in range(count0+count1,count0+count1+count2):
            nums[i] = 2
        return nums