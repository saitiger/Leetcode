class Solution:
    def minPairSum(self, nums):
        nums.sort()
        s, e = 0, len(nums) - 1
        ans = float('-inf')
        while s < e:
            ans = max(ans, nums[s] + nums[e])
            s += 1
            e -= 1
        return ans
