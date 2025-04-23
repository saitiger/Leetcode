"""
The idea is to find pair with target sum equal to zero 
Have a max_zero_sum that keeps track of largest number seen so 
far with zero sum
"""
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = 0 
        seen = set()
        for n in nums:
            if -n in seen:
                ans = max(ans,abs(n))
            seen.add(n)
        return ans if ans!=0 else -1
