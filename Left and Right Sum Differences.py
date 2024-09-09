class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = []
        s,total = 0,sum(nums)
        ans = []
        for i in range(n):
            left_sum.append(s)
            right_sum = total - left_sum[i] - nums[i]
            val = abs(right_sum - left_sum[i])
            ans.append(val)
            s+=nums[i]
        return ans
