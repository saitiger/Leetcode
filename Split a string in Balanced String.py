class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt_R,cnt_L = 0,0
        cnt = 0
        for i in range(len(s)):
            if(s[i]=='R'):
                cnt_R+=1
            else:
                cnt_L+=1
            if(cnt_R==cnt_L):
                cnt+=1
        return cnt
