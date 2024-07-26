class Solution:
    def getAverages(self, nums, k):
# Solution 1 Sliding Window
        n = len(nums)
        if k == 0:
            return nums
        res = [-1] * n
        if n < 2 * k + 1:
            return res
        s = 0
        l = 0
        r = 2 * k
        i = k
        for j in range(l,r+ 1):
            s+=nums[j]
        res[i] = s//(2 * k + 1)
        i+= 1
        r+= 1
        while r < n:
            s = s - nums[l] + nums[r]
            res[i] = s // (2 * k + 1)
            i+= 1
            l+= 1
            r+= 1
        return res
# Solution 2 Prefix Sum
        n = len(nums)
        if k == 0:
            return nums
        result = [-1] * n
        if n < 2 * k + 1:
            return result
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        for i in range(k, n - k):
            left_idx = i - k
            right_idx = i + k
            total_sum = prefix_sum[right_idx]
            if left_idx > 0:
                total_sum -= prefix_sum[left_idx - 1]
            result[i] = total_sum // (2 * k + 1)
        return result
