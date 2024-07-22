class Solution:
    def minimumOperations(self, nums, target):
        n = len(nums)
        result,prev = 0,0
        for i in range(n):
            curr = target[i] - nums[i]
            if (curr > 0 and prev < 0) or (curr < 0 and prev > 0):
                result += abs(curr)
            elif abs(curr) > abs(prev):
                result += abs(curr - prev)
            prev = curr
        return result
