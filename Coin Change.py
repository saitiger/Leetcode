class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Greedy Solution doesn't work
        # coins.sort()
        # i = len(coins)-1
        # cnt = 0
        # while amount>0 and i>=0:
        #     if(amount>=coins[i]):
        #         amount-=coins[i]
        #         cnt+=1
        #     else:
        #         i-=1
        # return cnt if amount==0 else -1
        
        dp  = [0] * (amount+1)

        # Dynamic Programming
        
        def changeHelper(left):
            if left == 0:
                return 0
            
            if dp[left]:
                return dp[left]

            options = []
            for c in coins:
                if c <= left:
                    v = changeHelper(left - c)         
                    if v != -1:
                        options.append(v+1)
            
            v = -1 if not options else min(options)
            dp[left] = v
            return dp[left]

        return changeHelper(amount)
