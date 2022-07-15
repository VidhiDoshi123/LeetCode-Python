class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy=nums[:]
        nums_copy.sort()
        i=0
        start=math.inf
        end=0
        for i in range(len(nums)):
            if(nums[i]!=nums_copy[i]):
                start=min(start,i)
                end=max(end,i)
        print(start,end)
        if(start<=end):
            return (end-start+1)
        else:
            return 0