class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt,max_cnt = 0,0
        i,j=0,0
        while j<len(s):
            if s[j] in 'aeiou':
                cnt+=1
            if(j-i+1==k):
                max_cnt = max(max_cnt,cnt)
                if(s[i] in 'aeiou'):
                    cnt-=1
                i+=1
            if(max_cnt==k):
                return k
            j+=1
        return max_cnt
