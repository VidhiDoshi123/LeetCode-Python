class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        h1=[0]*26
        h2=[0]*26
        if(n>len(s2)):
            return False
        for c in s1:
            h1[ord(c)-ord('a')]+=1
        i=0
        for i in range(len(s2)):
            if(i<n):
                h2[ord(s2[i])-ord('a')]+=1
            else:
                h2[ord(s2[i])-ord('a')]+=1
                h2[ord(s2[i-n])-ord('a')]-=1
            if(h1==h2):
                return True
        return False
        