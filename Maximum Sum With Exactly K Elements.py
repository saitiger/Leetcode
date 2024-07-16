class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        if k==1:
            return max(nums)
        else:
            return int(max(nums)*k + (k*(k-1))/2)
