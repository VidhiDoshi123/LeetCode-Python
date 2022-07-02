class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart=0
        ans=set()
        maxLen=0
        for windowEnd in range(len(s)):
            while(s[windowEnd] in ans):
                ans.remove(s[windowStart])
                windowStart+=1
            ans.add(s[windowEnd])
            maxLen=max(maxLen,windowEnd-windowStart+1)
        return maxLen