class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        s = 0
        for n in nums:
            s += n
            if s > max_sum:
                max_sum = s   
            if s < 0:
                s = 0
        return max_sum
