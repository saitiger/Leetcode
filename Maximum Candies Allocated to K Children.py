class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_distr(candies: List[int], mid: int, k: int) -> bool:
            for candy in candies:
                k -= candy // mid
                if k <= 0:  
                    return True  
            return k <= 0  

        if sum(candies) < k:
            return 0
        
        l, r = 1, max(candies)
        result = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if can_distr(candies, mid, k):
                result = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return result
