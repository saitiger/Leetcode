class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        l = r = 0
        flag = 0
        while r<len(nums):
            if(nums[r]==0):
                flag+= 1
            while(flag>1):
                if(nums[l]==0):
                    flag-=1
                l+=1
            max_len = max(max_len,(r-l+1))
            r+=1
        return max_len - 1
