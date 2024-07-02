class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1 
        while (i<len(nums) and j <len(nums)):
            if(nums[i]==nums[j]):
                j = j+1
                i = i+1
            elif(nums[i]!=nums[j]):
                nums[i],nums[j] = nums[j],nums[i]
                j = j+1
        return i+1
