#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        hmap = {}
        for i in range(n):
            if(arr[i] not in hmap):
                hmap[arr[i]] = 1
            else:
                hmap[arr[i]] = hmap[arr[i]] + 1
        for i in range(n):
            if(hmap[arr[i]] == 1):
                return arr[i]
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends