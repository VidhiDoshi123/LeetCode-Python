class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                left=b+1
                right=len(nums)-1
                while(left<right):
                    if(nums[a]+nums[b]+nums[left]+nums[right]==target):
                        ans.add((nums[a],nums[b],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif(nums[a]+nums[b]+nums[left]+nums[right]<target):
                        left+=1
                    else:
                        right-=1
        return ans