class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left=0
        product=1
        right=0
        ans=0
        for right in range(len(nums)):
            product=product*nums[right]
            while(product>=k and left<len(nums)):
                product=product/nums[left]
                left+=1
            if(left<=right):
                ans+=(right-left)+1
        return ans