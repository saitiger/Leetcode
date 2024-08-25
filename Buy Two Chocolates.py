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

# Optimal (Leetcode Editorial)
        minimum = min(prices[0], prices[1])
        second_minimum = max(prices[0], prices[1])
        for i in range(2, len(prices)):
            if prices[i] < minimum:
                second_minimum = minimum
                minimum = prices[i]
            elif prices[i] < second_minimum:
                second_minimum = prices[i]
        min_cost = minimum + second_minimum
        if min_cost <= money:
            return money - min_cost
        return money
