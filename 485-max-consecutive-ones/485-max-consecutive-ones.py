class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        i=0
        j=0
        while(i<len(nums)):
            if(j<=len(nums)-1):
                j = i+1
            if(nums[i] ==1):
                count =1
                while(j<=len(nums)-1 and nums[j]==1):
                    j+=1
                    count+=1
            
            if(count > max_count):
                i = i+ count
                max_count = max(max_count,count)
            else:
                i+=1

        return max_count