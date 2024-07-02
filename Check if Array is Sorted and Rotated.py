class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0 
        for i in range(len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]):
                flag+=1
            # if(nums[i-1]>nums[i]):
            #     flag+=1
        return flag<=1
