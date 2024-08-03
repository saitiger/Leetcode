class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]
        
        result = [0] * n
        
        for i in range(n):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = prefix_sum[n - 1] - prefix_sum[i]
            
            left_count = i
            right_count = n - i - 1
            
            left_total = (left_count * nums[i]) - left_sum
            right_total = right_sum - (nums[i] * right_count)
            
            result[i] = left_total + right_total
        
        return result
