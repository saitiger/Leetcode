class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn = nums[0]
        ans = -1
        for i in range(1,len(nums)):
            if nums[i]>minn:
                ans = max(ans,nums[i]-minn)
            else:
                minn = nums[i]
        return ans
