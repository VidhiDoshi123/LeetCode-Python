class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket={}
        windowStart=0
        maxFruit=0
        for windowEnd in range(len(fruits)):
            curFruit = fruits[windowEnd]
            if(curFruit not in basket):
                basket[curFruit]=1
            else:
                basket[curFruit]+=1
            while(len(basket) >2):
                remove= fruits[windowStart]
                basket[remove]-=1
                if(basket[remove]==0):
                    del basket[remove]
                windowStart+=1
            maxFruit=max(maxFruit,windowEnd-windowStart+1)
        return maxFruit