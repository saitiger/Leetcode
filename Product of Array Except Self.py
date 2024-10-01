class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1] # Prefix i.e product of all elements to the left of the current element 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Traverse right to left to find postfix of the current element 
            res[i] *= postfix # Product of all the elements to the right 
            postfix *= nums[i] # Store the postfix for the next iteration 
        return res
