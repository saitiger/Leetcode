class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):
            correct_idx = nums[i] - 1 
            if(correct_idx<len(nums) and nums[i]!=nums[correct_idx]):
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
            else:
                i+=1
        for j in range(len(nums)):
            if(nums[j]!=j+1):
                return nums[j]
