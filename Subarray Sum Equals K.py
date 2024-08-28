class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        s = 0
        prefix_sum = {}
        prefix_sum[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            if s-k in prefix_sum:
                cnt += prefix_sum[s-k]
            prefix_sum[s] = prefix_sum.get(s, 0)+1
        return cnt
