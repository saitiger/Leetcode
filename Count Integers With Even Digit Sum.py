class Solution:
    def countEven(self, num: int) -> int:
        cnt=0
        for i in range(2,num+1):
            if i<=9 and i%2==0:
                cnt+=1
            elif i>=10:
                s = 0 
                n = i 
                while n!=0:
                    s+=n%10
                    n = n//10
                if s%2==0:
                    cnt+=1
        return cnt
