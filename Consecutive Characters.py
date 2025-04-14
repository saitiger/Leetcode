class Solution:
    def maxPower(self, s: str) -> int:
        max_cnt = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1  
        return max_cnt

# Two Pointer 
class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        max_cnt = 1
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            max_cnt = max(max_cnt, j - i)
            i = j 
        return max_cnt
