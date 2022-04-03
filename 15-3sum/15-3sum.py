class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()
        for i in range(0,len(nums)-2):
            start = i+1
            end = len(nums) -1
            while(start<end):
                current_sum = nums[i] + nums[start] + nums[end]
                if(current_sum == 0):
                    if [nums[i],nums[start],nums[end]] not in ans:
                        ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                elif(current_sum < 0):
                    start+=1
                else:
                    end-=1
           
            
        return ans