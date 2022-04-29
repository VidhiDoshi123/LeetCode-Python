#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
	    ans = []
        def subsetSum(index,sum):
            if(index == N):
                ans.append(sum)
                return
            subsetSum(index+1,sum+arr[index])
            subsetSum(index+1,sum)
        subsetSum(0,0)
        ans.sort()
        return ans
            
            
                
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends