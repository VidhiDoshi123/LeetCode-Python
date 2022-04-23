#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        #sort acc to highest value
        Items.sort(key=lambda x:(x.value/x.weight),reverse=True)
        profit= 0
        current_capacity=0
        for item in Items:
            if(current_capacity+item.weight<=W):
                current_capacity+=item.weight
                profit+=item.value
            else:
                balance= W-current_capacity
                profit+=(item.value)*(balance/item.weight)
                break
        return profit
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends