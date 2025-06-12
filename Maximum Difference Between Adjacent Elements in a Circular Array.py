class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)  
        i = 0 
        j = 1 
        res = float('-inf')
        
        while i < n:  
            if abs(nums[j % n] - nums[i % n]) > res:
                res = abs(nums[j % n] - nums[i % n])
            i += 1
            j += 1
        
        return res
