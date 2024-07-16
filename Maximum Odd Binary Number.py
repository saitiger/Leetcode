class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_1 = 0
        n = len(s)
        for d in s:
            if(d==1):
                cnt_1+=1
        return '1' * (cnt_1 - 1) + '0' * (n - cnt_1) + '1'
