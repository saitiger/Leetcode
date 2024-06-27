class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if m > 0 and nums[m] < nums[m-1]: # If the element on the left side i.e. previous element is greater then we have the chance of finding peak on the left side
              r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m+1]: 
              l = m + 1 
            else: # If neither left nor right are greater then we have found the peak element
                break 
        return m
