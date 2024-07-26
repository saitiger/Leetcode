class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r =0,len(nums) - 1
        idx = len(nums) - 1
        res = [0] * len(nums)
        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                res[idx] = nums[l] ** 2
                l+=1
            else:
                res[idx] = nums[r] ** 2
                r-=1
            idx-= 1
        return res
