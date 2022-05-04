class Solution:
    def helper(self,nums,res,path):
        path.sort()
        if(path not in res):
            res.append(path)
        for i in range(len(nums)):
            self.helper(nums[i+1:],res,path+[nums[i]])
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums,res,[])
        return res
        