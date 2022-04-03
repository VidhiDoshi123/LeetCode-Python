class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        hashmap ={}
        for i in range(len(nums)):
            num = nums[i]
            target = - num
            for j in range(i+1,len(nums)):
                complement = target - nums[j]
                if(complement in hashmap and hashmap[complement]!=j):
                    sublist = list()
                    sublist.append(nums[i])
                    sublist.append(nums[j])
                    sublist.append(complement)
                    sublist.sort()
                    if(sublist not in ans):
                        ans.append(sublist)
            hashmap[nums[i]] = i
        return ans