class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        num_chocolates = 2
        i = 0
        res = money 
        while num_chocolates>0 and res>0:
            res-=prices[i]
            num_chocolates-=1
            i+=1
        return res if res>=0 and num_chocolates==0 else money
