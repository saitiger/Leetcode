class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l,r,flip,ans=0,0,0,0

        while r<len(nums):
            if nums[r]==0:
                flip+=1

            while flip>k:
                if nums[l]==0:
                    flip-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
