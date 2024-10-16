class Solution(object):
    def kthFactor(self, n, k):
        factor_num = 0
        for i in range(1,n+1):
            if n % i == 0 :
                factor_num+=1
                if factor_num == k: return i
        return -1
        
