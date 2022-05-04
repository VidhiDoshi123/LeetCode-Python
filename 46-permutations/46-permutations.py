class Solution:
    def helper(self,nums,res,path):
        if(len(nums)==0):
            res.append(path)
            return
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:],res,path+[nums[i]])
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums,res,[])
        return res