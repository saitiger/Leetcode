# Solution 1 : Binary Search 
class Solution:
    # Checking if the max value is possible 
    def isValid(self, nums: List[int], mid_max: int, n: int) -> bool:
        arr = nums[:] # Creating a copy of nums array since modification of array takes inplace 
        for i in range(n-1):
            if arr[i] > mid_max: # If element is larger than the mid_max value then return False
                return False
            buffer = mid_max - arr[i] # Buffer refers to the value that value to the decreased can be increased based on the current iteration of max 
            arr[i+1] -= buffer # Reduce i+1 value by the buffer value
        return arr[n-1] <= mid_max # Checking if last element is also valid i.e. arr[n-1] is less than or equal to the current iteration of max 
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxL = 0
        maxR = max(nums)
        result = 0
        while maxL <= maxR:
            mid_max = maxL + (maxR - maxL) // 2
            if self.isValid(nums, mid_max, n): # If valid then store the result and search for even smaller value
                result = mid_max
                maxR = mid_max - 1
            else:
                maxL = mid_max + 1 # If not valid look for larger value
        return result

# Solution 2 (Credit : Neetcode)
# The idea behind the solution is that we need to distribute the sum of all values between the numbers and the the value can only be shifted left to right 
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = nums[0] # First value can remain the same or be incremented hence it is the bottleneck.
        for i in range(1,len(nums)):
            total+=nums[i] # Prefix sum to calculate the running sum 
            res = max(res,math.ceil(total/(i+1))) # Distributing the values between the terms
        return res
