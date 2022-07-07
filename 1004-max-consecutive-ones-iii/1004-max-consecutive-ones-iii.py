class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count={}
        start=0
        freq=0
        res=0
        for end in range(len(nums)):
            if(nums[end]==0):
                freq+=1
            while(freq>k):
                if(nums[start]==0):
                    freq-=1
                start+=1
            res=max(res,end-start+1)
        return res
        
        return res