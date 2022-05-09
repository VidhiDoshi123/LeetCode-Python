class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False
        for i in range(0,len(nums)-1):
            if(nums[i]>nums[i+1] and not flag):
                flag= True
            elif(nums[i] >nums[i+1] and flag):
                return False
        if(nums[len(nums)-1]>nums[0] and flag):
            return False
        
        return True