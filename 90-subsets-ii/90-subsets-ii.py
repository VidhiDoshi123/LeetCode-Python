class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset(index,ans,ds):
            ans.append(ds.copy())
            for i in range(index,len(nums)):
                if(i!=index and nums[i]== nums[i-1]):
                    continue
                ds.append(nums[i])
                subset(i+1,ans,ds)
                ds.pop(-1)
        ds = list()
        ans = list()
        nums.sort()
        subset(0,ans,ds)
        return ans
        