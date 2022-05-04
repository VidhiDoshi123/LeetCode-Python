class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates,target,res,[])
        return res
    
    def helper(self,candidates,t,res,path):
        if(t==0):
            res.append(path)
            return
        for i in range(len(candidates)):
            if(candidates[i] > t):
                continue
            self.helper(candidates[i:],t-candidates[i],res,path+[candidates[i]])