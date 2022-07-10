class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h1=[0]*26
        h2=[0]*26
        res=[]
        n=len(p)
        for c in p:
            h1[ord(c)-ord('a')]+=1
        print(h1)
        i=0
        for i in range(len(s)):
            print('in i',i)
            if(i<n):
                h2[ord(s[i])-ord('a')]+=1
            else:
                h2[ord(s[i])-ord('a')]+=1
                h2[ord(s[i-n])-ord('a')]-=1
            print(h2)   
            if(h1==h2):
                print('here')
                if(i<n):
                    res.append(n-i-1)
                else:
                    res.append(i-n+1)
        return res