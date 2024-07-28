class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Without loop or recursion
        if n<=0:
            return False
        return log(n,4)%1==0

        # if n==1:
        #     return True
        # if n<=0 or n%4!=0:
        #     return False
        # return self.isPowerOfFour(n//4)
