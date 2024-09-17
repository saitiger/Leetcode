# Solution 1 
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,0 
        cnt = 0 

        while r < len(nums) and l< len(nums):
            while r<len(nums) and nums[r] - nums[l]<=k:
                r+=1
            l = r
            cnt+=1
        return cnt

# Solution 2 : Use the same approach and a different way of writing the code.
# i.e. If difference of starting and current element of subsequence is greater than K, then only start new subsequence

        nums.sort()
        ans = 1
        start = nums[0]
        for i in range(1, len(nums)):
            diff = nums[i] - start
            if diff > k:
                ans += 1
                start = nums[i]
        
        return ans
