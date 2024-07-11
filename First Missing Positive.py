class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            correctIdx = nums[i]-1
            if nums[i]>0 and nums[i]<n and nums[i]!=nums[correctIdx]:
                nums[i], nums[correctIdx] = nums[correctIdx], nums[i]
            else:
                i+= 1
  
        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1
