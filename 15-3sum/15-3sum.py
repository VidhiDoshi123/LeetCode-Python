class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for k in range(len(nums)-2):
            i=k+1
            j=len(nums)-1
            target=-(nums[k])
            while(i<j):
                if(nums[i]+nums[j]==target):
                    ans.add((nums[i],nums[j],nums[k]))
                    i+=1
                    j-=1
                elif(nums[i]+nums[j]<target):
                    i+=1
                else:
                    j-=1
        return ans