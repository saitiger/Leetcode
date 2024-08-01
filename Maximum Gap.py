from math import ceil

class Solution:
    def maximumGap(self, nums):
        max_gap = 0
        n = len(nums)
        if n < 2:
            return 0

        min_val = float('inf')
        max_val = float('-inf')

        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)

        bucket_size = ceil((max_val - min_val) / (n - 1))
        min_of_bucket = [float('inf')] * (n - 1)
        max_of_bucket = [float('-inf')] * (n - 1)

        for num in nums:
            if num == min_val or num == max_val:
                continue
            bucket_index = (num - min_val) // bucket_size
            min_of_bucket[bucket_index] = min(min_of_bucket[bucket_index], num)
            max_of_bucket[bucket_index] = max(max_of_bucket[bucket_index], num)

        for i in range(n - 1):
            if max_of_bucket[i] == float('-inf'):
                continue
            max_gap = max(min_of_bucket[i] - min_val, max_gap)
            min_val = max_of_bucket[i]

        max_gap = max(max_gap, max_val - min_val)
        return max_gap
