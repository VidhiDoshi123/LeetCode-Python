class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            j=nums[i]
            if(nums[i]<len(nums) and i!=nums[i]):
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if(i!=nums[i]):
                return i
        return len(nums)