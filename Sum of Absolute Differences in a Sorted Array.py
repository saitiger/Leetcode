# The intuition behind the solution is for each element we need to calculate 
# sum(nums[i] - nums[0], nums[i]-nums[1] ... nums[i] - nums[i] , nums[i]- nums[i+1] ... nums[i] - nums[n-1])
# which can be simplified to nums[i]*i - (nums[0]+nums[1]+nums[2]+...nums[i-1]) i.e. length of array till i'th element times nums[i] - sum of elements till element
# i excluding the element itself plus (nums[i+1] + nums[i+2] + nums[i+3] + ...) - nums[i] * (n-i-1) 

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1] # Running Sum i.e. Sum of all elements to the left including the element itself.
        
        result = [0] * n
        
        for i in range(n):
            left_sum = prefix_sum[i] - nums[i] # Exclude the element to compute left sum
            right_sum = prefix_sum[n - 1] - prefix_sum[i] # Right Sum is Total - left_sum - nums[i] which is prefix of last element - prefix of the current element 
            
            left_count = i # Size of the subarray for the left part 
            right_count = n - i - 1 # Size of the subarray for the right part 
            
            left_total = (left_count * nums[i]) - left_sum # Sum of elements to the left 
            right_total = right_sum - (nums[i] * right_count) # Sum of elements to the right 
            
            result[i] = left_total + right_total
        
        return result
