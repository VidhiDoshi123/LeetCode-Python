class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged=[]
        if(len(intervals)<2 and len(newInterval)==0):
            merged.append(newInterval)
            return merged
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if(not merged or interval[0]>merged[-1][1]):
                merged.append(interval)
            elif(interval[0]<=merged[-1][1]):
                merged[-1][1]=max(interval[1],merged[-1][1])
        return merged