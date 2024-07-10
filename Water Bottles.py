# Solution 1 
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles
        while empty >= numExchange:
            extra = empty // numExchange
            remain = empty % numExchange
            ans+= extra
            extra = remain + extra
        return and

# Solution 2
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles>=numExchange:
            ans+=numExchange
            numBottles-= numExchange
            numBottles+= 1
        return ans+numBottles
