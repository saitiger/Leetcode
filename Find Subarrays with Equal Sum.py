class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return False
        seen = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1] # Sum of two consequtive elements 
            if s in seen:
                return True # If sum is already seen return True 
            seen.add(s) # If not seen already add it to the set 
        return False    
