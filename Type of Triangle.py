class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sum of any two sides should be greater than or equal to the third side to be valid
        if nums[0]+nums[1]<=nums[2] and nums[0]+nums[2]<=nums[1] and nums[1]+nums[2]<=nums[0]:
            return "none"
        else:
            len_set = set(nums)
            if len(len_set)==1:
                return "equilateral"
            elif len(len_set)==2:
                return "isosceles"
            else:
                return "scalene"
