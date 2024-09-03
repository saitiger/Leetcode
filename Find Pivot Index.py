# Iteratively calculate the prefix/lsum. Check if lsum is equal to rsum if not add the current element to lsum and continue 
# the loop
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            r_sum -= nums[i] # Total - current element 
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
