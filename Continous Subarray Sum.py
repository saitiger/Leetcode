class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        
        remainder_map = {0: -1}
        total_sum = 0
        
        for i in range(n):
            total_sum += nums[i]
            remainder = total_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
                
        return False
