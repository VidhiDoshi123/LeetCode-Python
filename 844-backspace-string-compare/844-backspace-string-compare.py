class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackA=[]
        stackB=[]
        for c in s:
            if(c =="#" and len(stackA)!=0):
                stackA.pop(-1)
            elif(c!="#"):
                stackA.append(c)
        for c in t:
            if(c =="#" and len(stackB)!=0):
                stackB.pop(-1)
            elif(c!="#"):
                stackB.append(c)
        print(stackA,stackB)
        return stackA == stackB