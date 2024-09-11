class Solution:
    def reductionOperations(self, nums):
        n = len(nums)
        nums.sort()
        
        count = 0
        
        for i in range(n - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                continue
            
            count += n - i
        
        return count
