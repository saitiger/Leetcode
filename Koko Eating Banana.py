import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = l + (r-l)// 2 # Avoinding Overflow

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k) # Checking if eating rate is sufficient 
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
