# The intuition is that we find the same mod again if and only if we have encountered elements 
# that sum up to a multiple of k

class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        
        remainder_map = {0: -1} # Initialze to account for an empty array because 0 is a multiple of k 
        total_sum = 0
        
        for i in range(n):
            total_sum += nums[i]
            remainder = total_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2: # Validating if the size of the contiguous array has a size greater 
                                                      # than or equal to 2 
                    return True
            else:
                remainder_map[remainder] = i
                
        return False
