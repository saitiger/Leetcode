class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []     
        i = 0 
        while i < len(nums): 
            initial = nums[i]  
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            if initial!= nums[i]: 
                res.append(str(initial) + "->" + str(nums[i]))
            else: 
                res.append(str(nums[i]))
            i += 1
        return res
