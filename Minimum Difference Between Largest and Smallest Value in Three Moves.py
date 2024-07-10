class Solution:
    def minDifference(self, nums: List[int]) -> int:
      # Solution 1
      if len(nums)<=4:
            return 0
        nums.sort()
        ans = float('inf')
        for l in range(4):
            r = len(nums)-4+l
            ans = min(ans,nums[r]-nums[l])
        return ans
      # Solution 2 
      if len(nums)<=4:
            return 0
        min_4 = sorted(heapq.nsmallest(4,nums))
        max_4 = sorted(heapq.nlargest(4,nums))
        ans = float('inf')
        for i in range(len(min_4)):
            ans = min(ans,max_4[i]-min_4[i])
        return ans
