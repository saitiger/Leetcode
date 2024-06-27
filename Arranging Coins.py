class Solution:
    def arrangeCoins(self, n: int) -> int:
    #    i = 1 
    #    rem = n
    #    idx = 0
    #    while i<=n:
    #     if(rem>0):
    #         rem = rem-i
    #         i+=1
    #     idx = max(i,idx)
    #     return i

    # Brute Force : subract coins and as soon as we go below zero that is the maximum number of rows we can make with 
    # given number of coins
      
    # if n == 1:
    #     return 1
        
    # for i in range(1, n + 1):
    #     n -= i
    #     if (n < 0):
    #         return i - 1

    # Binary Search : Using the fact that sum on natural numbers is n(n+1)/2 we can calculate total number of rows using 
    # binary search

        l, r = 1, n
        ans = 0
        while l <=r:
            mid = l + (r-l)//2
            coins = (mid /2) * (mid+1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                ans = max(mid, ans)
        return ans
