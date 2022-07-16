class Solution:
    def isHappy(self, n: int) -> bool:
        ans=[]
        def square_num(n):
            summ=0
            while(n):
                summ +=(n%10)*(n%10)
                n=n//10
            return summ
        while(True):
            squared_num=square_num(n)
            print(squared_num)
            if(squared_num in ans):
                return False
            elif(squared_num == 1):
                return True
            else:
                ans.append(squared_num)
                n=squared_num
        return False