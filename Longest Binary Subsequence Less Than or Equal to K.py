class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        i = len(s) - 1
        count = 0
        picked = 0
        curr = 0  
        while i>=0:
            if curr+int(s[i])*math.pow(2,picked)<=k: 
                count+=1
                curr = curr+int(s[i])*math.pow(2,picked)
                picked+=1
            i-=1
        return count
