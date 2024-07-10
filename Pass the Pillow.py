class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        p = dir = 1
        # dir = 1
        while time>0:
            time-=1
            p = p+dir
            if(p==1 or p==n):
                dir*=-1
        return p

      # Solution 2 
      full_pass = time//(n-1)
        rem = time%(n-1)
        if(full_pass%2!=0):
            return n - rem
        else:
            return 1 + rem
