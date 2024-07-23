class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        res = [True,True]
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                res[0] = False

        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                res[1] = False

        if (any(res)): return True
        else: return False

# Solution 2 
      if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            return True 
        return False
        
