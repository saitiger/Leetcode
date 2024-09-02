class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        minn = prices[0]
        res = 0
        for i in range(1,len(prices)):
            profit = prices[i] - minn
            minn = min(minn,prices[i])
            res = max(profit,res)
        return res
