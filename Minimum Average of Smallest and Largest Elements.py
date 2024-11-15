class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = float('inf')
        nums.sort()
        i,j = 0,len(nums)-1

        while i<len(nums) and j>0:
            ans = min(ans,(nums[i]+nums[j])/2)
            i+=1
            j-=1
        return ans
