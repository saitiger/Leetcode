class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cnt = 0

        for i in range(len(nums)):
            if (cnt==0):
                res = nums[i]
            if (nums[i] == res): 
                cnt+=1
            else:
                cnt-=1
        return res 
