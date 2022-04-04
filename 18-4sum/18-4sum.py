class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            target_3 = target - nums[i]
            for j in range(i+1,len(nums)-2):
                if(j==0 or (j>0)):
                    b = nums[j]
                    low = j+1
                    high = len(nums)-1
                    target_2 = target_3 - b
                    while(low<high):
                        if(nums[low]+nums[high]==target_2):
                            if([nums[i],b,nums[low],nums[high]] not in ans):
                                ans.append([nums[i],b,nums[low],nums[high]])
                            while(low<high and nums[low]==nums[low+1]):
                                low+=1
                            while(low<high and nums[high]==nums[high-1]):
                                high-=1
                            low +=1
                            high-=1
                        elif(nums[low]+nums[high]<target_2):
                            low+=1
                        else:
                            high-=1
        return ans
                    