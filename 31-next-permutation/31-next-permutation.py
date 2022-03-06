class Solution:
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index1 = index2= len(nums) - 2
        flag = False
        for i in range(index1,-1,-1):
            print("hello")
            if(nums[i] < nums[i+1]):
                index1= i
                flag = True
                break
        print(flag)
        if(not flag):
            return nums.sort()
        num1 = nums[index1]
        for i in range(len(nums)-1,0,-1):
            if(num1 < nums[i]):
                index2 = i
                num2 = nums[index2]
                break
        print(nums[index1],nums[index2],index1)
        nums[index1],nums[index2] = nums[index2], nums[index1]
        print("-------")
        print(index1 + 1)
        i = index1 + 1
        j = len(nums) -1
        print("**********")
        print(i,j)
        while(i < len(nums) -1 and j >=index1+1 and i < j):
            nums[i],nums[j] = nums[j] , nums[i]
            i = i +1
            j = j -1
            
        