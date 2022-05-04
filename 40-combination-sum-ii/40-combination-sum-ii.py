class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(candidates,target,res,[])
        return res
    def helper(self,nums,target,res,path):
        if(target==0):
            res.append(path)
        
        for i in range(len(nums)):
            if(nums[i] > target):
                break
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            self.helper(nums[i+1:],target-nums[i],res,path+[nums[i]])