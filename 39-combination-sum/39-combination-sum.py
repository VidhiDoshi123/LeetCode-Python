class Solution:
    def findComb(self,index,candidates,target,ans,ds):
        if(index==len(candidates)):
            if(target==0):
                ans.append(ds.copy())
            return
        if(candidates[index]<=target):
            ds.append(candidates[index])
            self.findComb(index,candidates,target-candidates[index],ans,ds)
            ds.pop(-1)
        self.findComb(index+1,candidates,target,ans,ds)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        ds = list()
        self.findComb(0,candidates,target,ans,ds)
        return ans