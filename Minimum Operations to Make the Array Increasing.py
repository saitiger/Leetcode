class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        cnt = 0

        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                res=nums[i-1]-nums[i]+1
                nums[i]+=res
                cnt+=res
            else:
                continue
        return cnt 
