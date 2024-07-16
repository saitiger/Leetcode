class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range(1,len(nums)):
            if(farthest<i):
                return False
            farthest = max(i+nums[i],farthest)
        return True
