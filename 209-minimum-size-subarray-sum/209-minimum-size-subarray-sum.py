class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL=math.inf
        n=len(nums)
        start=0
        end=0
        cur_sum=nums[0]
        while(end<n):
            if(cur_sum>=target):
                minL=min(minL,end-start+1)
                cur_sum-=nums[start]
                start+=1
            else:
                end+=1
                if(end<n):
                    cur_sum+=nums[end]
        if(minL==math.inf):
            return 0
        else:
            return minL